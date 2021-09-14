from django.shortcuts import render, HttpResponse
from .models import Articles

# Create your views here.

def search(request):
    return render(request,'article/search_articles.html')

def search_data(request):
    if request.GET['articles_text']:
        articulo = request.GET['articles_text']
        if len(articulo) > 20:
            message = 'Nombre de Aritulo muy extenso'
        else:
            data= Articles.objects.filter(section__icontains=articulo)
            return render(request,'article/results.html',{'articulos':data,'query':articulo})
    else:
        message = 'Valor vacio o no valido'
    return HttpResponse(message)