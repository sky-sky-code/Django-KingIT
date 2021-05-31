from django.urls import path
from .views import *

urlpatterns = [
    path('', managerC, name='home'),
    path('managerC_TC/search/', FilterTC.as_view(), name='search_managerC'),
    path('managerC_TC/add/', ManagerCAdd.as_view(), name='managerC_add'),
    path('managerC_TC/edit/<int:pk>/', edit_tc, name='managerC_edit'),
    path('managerC_TC/del/<int:pk>/', delete_tc, name='delete_tc'),
    path('managerC_pavilions/', managerC_pavilions, name='managerC_pavilions'),
    path('managerC_pavilions/search/', FilterPavilions.as_view(), name='pavilions_search'),
    path('administrator/', administrator, name='administrator'),
    path('administrator/search/', AdminSearch.as_view(), name='administrator_search'),
    path('administrator/add/', AdminADD.as_view(), name='administrator_add'),
    path('administrator/edit/<int:pk>/', admin_edit, name='administrator_edit'),
    path('administrator/del/<int:pk>/', delete_worker, name='delete_worker'),
]