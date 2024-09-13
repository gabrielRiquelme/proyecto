from django.http import HttpResponse
from django.shortcuts import render
from templates import * 

def saludo(request):
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
    return render(request,'users/login.html',{})