from django.shortcuts import render, redirect
from django.http import Http404
from .models import obtener_prendas, obtener_prenda_por_id, agregar_prenda
from .forms import PrendaForm

def prenda_list(request):
    query = request.GET.get('q', '').strip().lower()
    tipo = request.GET.get('tipo', '').strip()
    categoria = request.GET.get('categoria', '').strip()

    todas_prendas = obtener_prendas()
    prendas = todas_prendas

    # Filtro de búsqueda por texto (Nombre, Marca o Descripción)
    if query:
        prendas = [
            p for p in prendas
            if query in p['nombre'].lower() 
            or query in p['marca'].lower() 
            or query in p.get('descripcion', '').lower()
        ]

    # Filtro por Segmento / Público
    if tipo:
        prendas = [p for p in prendas if p.get('tipo') == tipo]

    # Filtro por Categoría
    if categoria:
        prendas = [p for p in prendas if p.get('categoria') == categoria]

    # Métricas para tarjetas de resumen
    total_catalogo = len(todas_prendas)
    total_stock_global = sum(p.get('stock', 0) for p in todas_prendas)
    total_activas = sum(1 for p in todas_prendas if p.get('disponible', False))

    contexto = {
        'titulo': 'Catálogo de Ropa Streetwear',
        'prendas': prendas,
        'query': request.GET.get('q', ''),
        'tipo_seleccionado': tipo,
        'categoria_seleccionada': categoria,
        'total_resultados': len(prendas),
        'total_catalogo': total_catalogo,
        'total_stock_global': total_stock_global,
        'total_activas': total_activas,
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