from django.shortcuts import render
from .models import obtener_prendas
# Create your views here.
def prenda_list(request):
    prendas = obtener_prendas()
    contexto = {
        'titulo' : 'Catálogo de Ropa StreetWear - UrbanTrend',
        'prendas' : prendas,
    }
    return render(request, 'store/prenda_list.html', contexto)