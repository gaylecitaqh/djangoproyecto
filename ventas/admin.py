from django.contrib import admin
from .models import Cliente, Poliza, Coberturas, ObjetoAsegurado

class ClienteAdmin(admin.ModelAdmin):
    search_fields = ('nombre',)

admin.site.register(Cliente,ClienteAdmin)

#se crea un modificador
class PolizaAdmin(admin.ModelAdmin):
    #los campos que van a mostrar en el url
    list_display = ('numpoliza','moneda','precio','estado')
    ordering = ('precio',)
    search_fields = ('numpoliza',)
    list_filter = ('estado',)

admin.site.register(Poliza,PolizaAdmin)


admin.site.register(Coberturas)
admin.site.register(ObjetoAsegurado)

# Register your models here.
