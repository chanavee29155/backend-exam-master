import django_filters

from apis.models import School


# code here
class SchoolFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = School
        fields = ('name',)
        
    