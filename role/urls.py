from django.urls import path
from .views import *

urlpatterns = [
    path('roles/', RoleList.as_view(), name='role-list'),
    path('roles/<int:pk>/', RoleDetail.as_view(), name='role-detail'),
    path('roles/create/', RoleCreate.as_view(), name='role-create'),
    path('roles/update/<str:name>/', RoleUpdate.as_view(), name='role-update'),
]