from rest_framework import serializers

from .models import Cliente, Poliza, ObjetoAsegurado

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
            model = Cliente
            fields="__all__"

class PolizaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poliza
        fields = "__all__"



class TipoObjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjetoAsegurado
        fields = '__all__'

#class CoberturaSerializer(serializer.Serializer):
 #           nombrecob = serializer.CharField(validators)