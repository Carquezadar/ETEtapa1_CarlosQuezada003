from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import Moneda, Contacto


class ContactoForm(forms.ModelForm):

    class Meta: 
        model= Contacto
        fields = ['NumIdentificaion', 'imagen','nombre', 'telefono', 'direccion', 'email' , 'pais','contraseña','moneda']
        labels ={
            'NumIdentificaion': 'Numero de Identificacion:', 
            'imagen':'Ingrese alguna imagen caracteristica',
            'nombre': 'Nombre completo:', 
            'telefono': 'Telefono:', 
            'direccion': 'Direccion:',
            'email': 'Email:',
            'pais': 'Pais:',
            'contraseña': 'Contraseña',
            'moneda': 'Moneda',
        }
        widgets={
            'NumIdentificaion': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Numero de Identificacion', 
                    'id': 'NumIdentificaion',
                    'name': 'NumIdentificaion',
                    
                    
                }
            ),
            'imagen':forms.ClearableFileInput(
                attrs={
                    'class': 'form-control',
                    'name': 'imagen',
                    'id': 'imagen',
                    'accept':"imagen/*"
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre', 
                    'id': 'nombre',
                    'name': 'nombre',
                } 
            ), 
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su telefono', 
                    'id': 'telefono',
                    'name': 'telefono',
                }
            ), 
            
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su direccion', 
                    'id': 'direccion',
                    'name': 'direccion',
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese email', 
                    'id': 'email',
                    'name': 'email',
                    'type': 'email',
                }
            ), 
            'pais': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese pais', 
                    'id': 'pais',
                    'name': 'pais',
                }
            ), 
            'contraseña': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese contraseña', 
                    'id': 'pais',
                    'name': 'contraseña',
                    'type': 'password'
                }
            ), 
            'moneda': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'moneda',
                    'name': 'moneda'
                }
            ),

        }