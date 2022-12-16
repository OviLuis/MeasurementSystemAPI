from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns



contact_list = ContactViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
contact_detail = ContactViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})