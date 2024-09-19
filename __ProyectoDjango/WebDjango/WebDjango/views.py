from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import login as lg
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import logout
from .forms import Registro
from django.contrib.auth.models import User

def index(request):
    return render(request,'index.html',{
        'mensaje':'Tienda',
        'titulo': 'Inicio',
        'productos':[
            {'titulo':'Campera','precio':15,'stock':False},
            {'titulo':'Pantalon','precio':11,'stock':True},
            {'titulo':'Remera','precio':18,'stock':False},
            {'titulo':'Gorra','precio':10,'stock':True}
        ]
    })

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        usuarios = authenticate(username=username,password=password)
        if usuarios:
            lg(request,usuarios)
            print('Logueado correctamente')
            messages.success(request,f'Bienvenido {usuarios.username}')
            return redirect('index')
        else:
            print('Usuario o contrasenia incorrectas')
            messages.error(request,'Datos incorrectos')

        print(username,'\n',password)
    return render(request,'users/login.html',{})

def salir(request):
    logout(request)
    messages.success(request,'Sesion cerrada')
    return redirect(login)

def register(request):
    form = Registro(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        username=form.cleaned_data.get('username')
        correo=form.cleaned_data.get('correo')
        password=form.cleaned_data.get('password')

        usuario = User.objects.create_user(username,correo,password)
        if usuario:
            lg(request,usuario)
            print(request,username)
            messages.success(request,f'Bienvenido {username}' )
            return redirect('index')

    return render(request,'users/registro.html',{
        'form':form
    })