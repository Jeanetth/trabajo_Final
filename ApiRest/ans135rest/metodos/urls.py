from django.urls import path
from . import views

urlpatterns = [
	path('unidad2/grafico/<str:expr>/', views.metodo_grafico, name='metodo_grafico'),
]
