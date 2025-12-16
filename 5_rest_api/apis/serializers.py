from rest_framework import serializers

from apis.models import School, Classroom, Teacher


class SchoolSerializer(serializers.ModelSerializer):
    address = serializers.CharField(required=False, allow_null=True, allow_blank=True)

    class Meta:
        model = School
        fields = '__all__'
    
    def validate(self, attrs):
        name = attrs.get('name')
        queryset = School.objects.filter(name=name)
        if self.instance is not None:
            queryset = queryset.exclude(id=self.instance.id)
        
        if queryset.exists():
            raise serializers.ValidationError(
                {
                    'detail': 'School name already exists'
                }
            )
        
        return attrs


class ClassroomSerializer(serializers.ModelSerializer):
    school_name = serializers.CharField(source='school.name', read_only=True)
    
    class Meta:
        model = Classroom
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(read_only=True)
    classrooms_detail = ClassroomSerializer(source='classrooms', many=True, read_only=True)
    
    class Meta:
        model = Teacher
        fields = '__all__'
    
    def validate(self, attrs):
        first_name = attrs.get('first_name')
        last_name = attrs.get('last_name')
        
        # Check if teacher with same first_name and last_name already exists
        queryset = Teacher.objects.filter(
            first_name=first_name,
            last_name=last_name
        )
        
        # If updating existing teacher, exclude current instance
        if self.instance is not None:
            queryset = queryset.exclude(id=self.instance.id)
        
        if queryset.exists():
            raise serializers.ValidationError(
                {
                    'detail': f'Teacher with name "{first_name} {last_name}" already exists'
                }
            )
        
        return attrs