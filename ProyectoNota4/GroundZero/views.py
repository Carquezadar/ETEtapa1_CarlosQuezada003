from django.shortcuts import redirect, render
from .models import Contacto
from .forms import ContactoForm

# Create your views here.

def home (request):
    return render(request, 'home.html',)

def crearContacto(request):
    contactos = Contacto.objects.all()
    if request.method=='POST': 
        contacto_form = ContactoForm(request.POST,request.FILES)
        if contacto_form.is_valid():
            contacto_form.save()
            return redirect('home')
    else:
        contacto_form= ContactoForm()
    return render(request, 'GroundZero/form_crearconsulta.html', {'contacto_form': contacto_form, 'datos':contactos})

def verContacto(request):
    contactos = Contacto.objects.all()
    if request.method=='POST': 
        contacto_form = ContactoForm(request.POST)
        if contacto_form.is_valid():
            contacto_form.save()
            return redirect('home')
    else:
        contacto_form= ContactoForm()
    return render(request, 'GroundZero/ver.html', {'contacto_form': contacto_form, 'datos':contactos})


def form_modificarconsulta(request,id):
    contactos = Contacto.objects.get(NumIdentificaion=id)

    datos={
        'form':ContactoForm(instance=contactos)
    }
    if request.method == 'POST':
        formulario = ContactoForm(request.POST, request.FILES, instance = contactos)
        if formulario.is_valid:
            formulario.save()
            return redirect('home')
    return render(request, 'GroundZero/form_modificarconsulta.html',datos)

def form_borrarconsulta(request,id):
    contactos = Contacto.objects.get(NumIdentificaion=id)
    contactos.delete()
    return redirect('home')