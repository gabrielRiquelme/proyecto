from django.http import HttpResponse

def saludo(request):
    return HttpResponse('Hola te saludo desde funcion de Django')