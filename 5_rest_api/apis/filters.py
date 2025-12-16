import django_filters

from apis.models import School, Classroom, Teacher, Student


class SchoolFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = School
        fields = ('name',)
        

class ClassroomFilter(django_filters.FilterSet):
    school = django_filters.CharFilter(method='filter_school', label='school')
    
    class Meta:
        model = Classroom
        fields = ('school',)
    
    def filter_school(self, queryset, name, value):
        return queryset.filter(school__name__icontains=value)


class TeacherFilter(django_filters.FilterSet):
    school = django_filters.CharFilter(method='filter_school', label='school')
    classroom = django_filters.CharFilter(method='filter_classroom', label='classroom')
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    last_name = django_filters.CharFilter(lookup_expr='icontains')
    gender = django_filters.ChoiceFilter(choices=[
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ])
    
    class Meta:
        model = Teacher
        fields = ('school', 'classroom', 'first_name', 'last_name', 'gender')
    
    def filter_school(self, queryset, name, value):
        return queryset.filter(classrooms__school__name__icontains=value)
    
    def filter_classroom(self, queryset, name, value):
        return queryset.filter(classrooms__id=value)


class StudentFilter(django_filters.FilterSet):
    school = django_filters.CharFilter(method='filter_school', label='school')
    classroom = django_filters.CharFilter(method='filter_classroom', label='classroom')
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    last_name = django_filters.CharFilter(lookup_expr='icontains')
    gender = django_filters.ChoiceFilter(choices=[
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ])
    
    class Meta:
        model = Student
        fields = ('school', 'classroom', 'first_name', 'last_name', 'gender')
    
    def filter_school(self, queryset, name, value):
        return queryset.filter(classroom__school__name__icontains=value)
    
    def filter_classroom(self, queryset, name, value):
        return queryset.filter(classroom__id=value)