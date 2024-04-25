from django.urls import path

from REP_App.views import add_unit, create_Tenant, create_property, home, prop_delete, prop_edit, tenant_delete, tenant_edit, viewall_property, viewall_tenant


urlpatterns = [
    path('home/',home,name ='home'),
    path('create_property/',create_property,name ='create_property'),
    path('create_tenant/',create_Tenant,name ='create_Tenant'),
    path('viewall_property/',viewall_property,name ='View_All_Property'),
    path('viewall_tenant/',viewall_tenant,name ='View_All_Tenant'),
    path('edit_property/<int:pk>/',prop_edit,name = 'prop_edit'),
    path('delete_property/<int:pk>/',prop_delete,name = 'prop_delete'),
    path('edit_tenant/<int:pk>/',tenant_edit,name = 'tenant_edit'),
    path('delete_tenant/<int:pk>/',tenant_delete,name = 'tenant_delete'),
    path('add_unit/',add_unit,name = 'add_unit'),



    
]