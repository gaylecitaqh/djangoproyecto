from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# el enrutador router manejará el put, get, post, etc
router = DefaultRouter()
router.register(r'clientes', views.ClienteViewSet)



urlpatterns = [
   # path('admin', views.index)
    path('contact/<str:name>',views.contact),
   # path('cliente/',views.cliente),
   #para el EJERCICIO 1
   # path('cliente/',views.cliente, name='cliente'),
    path('cliente/', views.ClienteCreateView.as_view(), name='cliente-create'),
    path('cliente/count/', views.cliente_count, name='cliente-count'),
    path('polizas/filtrar/estados/', views.polizas_estados, name='polizas-estados'),
   
   # path('poliza/reporte/', views.reporte_poliza, name='poliza-reporte'),
   #para el proyecto
    
    #path('cliente/',views.cliente, name="cliente"),
    #path('poliza/', views.polizaFormView, name="poliza"),
    #path('',views.index),


#las rutas que se van a generar se colocan en mis rutas en ventas
  #  path('', include(router.urls)),
]