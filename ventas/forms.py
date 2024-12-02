from django import forms
from .models import Poliza

#Django utiliza el tipo de dato ya modelado en la base y saca las propiedades
#mediante el siguiente form y lo convierte en html
class PolizaForm(forms.ModelForm):
    class Meta:
        model = Poliza
        fields = "__all__"