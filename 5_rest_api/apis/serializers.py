from rest_framework import serializers

from apis.models import School


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
            
        