from django.shortcuts import render, redirect
from django.http import Http404
from .models import obtener_prendas, obtener_prenda_por_id, agregar_prenda
from .forms import PrendaForm


def prenda_list(request):
    prendas = obtener_prendas()
    contexto = {
        'titulo': 'Catálogo de Ropa - UrbanTrend',
        'prendas': prendas,
    }
    return render(request, 'store/prenda_list.html', contexto)


def prenda_detail(request, prenda_id):
    prenda = obtener_prenda_por_id(prenda_id)
    if not prenda:
        raise Http404(f"La prenda con ID #{prenda_id} no existe.")

    return render(request, 'store/prenda_detail.html', {
        'prenda': prenda,
        'titulo': f"Detalle: {prenda['nombre']}",
    })


def prenda_create(request):
    if request.method == 'POST':
        form = PrendaForm(request.POST)
        if form.is_valid():
            nueva_prenda = {
                'nombre': form.cleaned_data['nombre'],
                'marca': form.cleaned_data['marca'],
                'tipo': form.cleaned_data['tipo'],
                'categoria': form.cleaned_data['categoria'],
                'talla': form.cleaned_data['talla'],
                'precio': float(form.cleaned_data['precio']),
                'stock': form.cleaned_data['stock'],
                'disponible': form.cleaned_data['disponible'],
                'descripcion': form.cleaned_data['descripcion'],
            }
            agregar_prenda(nueva_prenda)
            return redirect('store:list')
    else:
        form = PrendaForm()

    return render(request, 'store/prenda_form.html', {
        'titulo': 'Registrar Nueva Prenda',
        'form': form,
    })