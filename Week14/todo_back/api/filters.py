from django_filters import rest_framework as filters
from api.models import Task


class TaskFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')
    #complexity = filters.NumberFilter(lookup_expr='exact')
    status = filters.CharFilter(lookup_expr='contains')
    min_cmx = filters.NumberFilter(field_name='complexity', lookup_expr='gte')
    max_cmx = filters.NumberFilter(field_name='complexity', lookup_expr='lte')

    class Meta:
        model = Task
        fields = ('name', 'complexity', 'status',)