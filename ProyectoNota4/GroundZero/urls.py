from django.urls import path
from .views import home, crearContacto, verContacto, form_modificarconsulta, form_borrarconsulta

urlpatterns=[
    path('home', home, name='home'),
    path('crearContacto', crearContacto, name= 'crearContacto'),
    path('verContacto', verContacto, name= 'verContacto'),
    path('form_modificarconsulta/<id>', form_modificarconsulta, name='form_modificarconsulta'),
    path('form_borrarconsulta/<id>', form_borrarconsulta, name='form_borrarconsulta'),

]