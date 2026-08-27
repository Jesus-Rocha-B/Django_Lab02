from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.prenda_list, name='list'),
    path('nueva/', views.prenda_create, name='create'),
    path('<int:prenda_id>/', views.prenda_detail, name='detail'),
]