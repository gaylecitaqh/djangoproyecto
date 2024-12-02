from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .forms import PolizaForm
from .models import Cliente
from .forms import Poliza
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .serializers import ClienteSerializer,PolizaSerializer
#from .models import Cliente, Poliza
from rest_framework import generics

from .models import ObjetoAsegurado
from .serializers import TipoObjetoSerializer

from rest_framework.decorators import api_view



# Create your views here.
def index(request):
    return HttpResponse("Hola Mundo")

def contact(request, name):
    return HttpResponse(f"Hello {name}") #creando template

def cliente(request):
    post_nombre = request.POST.get("nombre")
    if post_nombre:
        q = Cliente(nombre=post_nombre)
        q.save()

    cliente = Cliente.objects.all()
    return render(request,"form_cliente.html", {
        "cliente": cliente
    }) # envia la informacion a la plantilla de template/cliente.html

def polizaFormView(request):
    form = PolizaForm()
    poliza = None
    #recibir el id que viene por parametros de la url
    id_poliza = request.GET.get("id")

    #usando función de django
    if id_poliza:
        poliza = get_object_or_404(Poliza, id=id_poliza)
        form = PolizaForm(instance=poliza) #instance sirve para inicializar el formulario con valores por defecto
    # el llamado es con http://127.0.0.1:8000/ventas/poliza/?id=2

    
    #Controlar el guardado
    if request.method=="POST":
        if poliza:
            form = PolizaForm(request.POST, instance=poliza)
        else:
            form = PolizaForm(request.POST)
    
    #validamos todo el formulario:
    if form.is_valid():
        form.save() # si todo está bien, graba el formulairo
    return render(request, "form_polizas.html",{"form": form})




class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


# con lo siguiente voy a controlar los métodos
class ClienteCreateView(generics.CreateAPIView,generics.ListAPIView):
    queryset=Cliente.objects.all()
    serializer_class = ClienteSerializer


@api_view(['GET']) # decorador
def cliente_count(request):
    try:
        cantidad = Cliente.objects.count()
        return JsonResponse({"cantidad": cantidad}, safe=False, status=200) #status : codigos de estado
    except Exception as e:
        return JsonResponse({"error": str(e)}, safe=False, status=500)

@api_view(['GET'])
def polizas_estados(request):
    try:
        poliza = Poliza.objects.filter(estado='c')
        return JsonResponse(PolizaSerializer(poliza, many=True).data, safe=False, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)}, safe=False, status=500)

"""
@api_view(['POST'])
def enviar_mensaje(request):
    cs = CoberturaSerializer(data=request.data)
    if cs.is_valid():
        return JsonResponse("mensaje": "Mensaje enviado correctamente")
    else:    
        return JsonResponse({"mensaje": cs.errors}, status=500)


@api_view(['GET'])
def reporte_poliza(request):
    try:
        polizas = Poliza.objects.filter(estados='u')
        return JsonResponse(ReportePolizaSerializer({"cantidad": polizas.count(), "polizas": polizas}).data, safe=False, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)}, safe=False, status=500)

    
    form = PolizaForm(request.POST)
    #validamos todo el formulario:
    if form.is_valid():
        form.save() # si todo está bien, graba el formulairo
    return render(request, "form_polizas.html",{"form": form})
    #se invoca con: http://127.0.0.1:8000/ventas/poliza/?id=1
    #  o con http://127.0.0.1:8000/ventas/poliza
"""

#def cliente(request):
 #   cliente = Cliente.objects.all()
 #   return render(request,"cliente.html", {
 #       "cliente": cliente
 #   }) # envia la informacion a la plantilla de template/cliente.html
#SE VE CON http://127.0.0.1:8000/ventas/cliente/?q=ana


#EJERCIO 1 PARA ENTREGAR
#def cliente(request):
#    query = request.GET.get('q')  # Capturamos el parámetro 'q' del request
#    cliente = Cliente.objects.filter(nombre__icontains=query)  # Filtramos por nombre
#    return render(request, 'cliente.html', {
#        'cliente': cliente
#    })
