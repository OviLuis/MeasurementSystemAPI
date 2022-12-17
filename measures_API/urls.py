from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .api_views import MeasureViewSet
from .views import index
from .views import download_csv_file


measures_list = MeasureViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
measures_detail = MeasureViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


urlpatterns = format_suffix_patterns([
    path('measures/', measures_list, name='measure-list'),
    path('measures/<int:pk>/', measures_detail, name='measure-detail'),
    path('', index, name='index'),
    path('download_csv_file/', download_csv_file, name='download-csv'),
])