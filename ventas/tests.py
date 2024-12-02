from django.test import TestCase
from .models import Cliente
from django.core.exceptions import ValidationError

# Create your tests here.

#ejecutará los test dentro de la aplicación inventario
class TestCliente(TestCase):
    def test_grabacion(self):
        cliente = Cliente(nombre="Bruno")
        cliente.save()
        self.assertEqual(Cliente.objects.count(), 1)# el valor debe ser igual al parametro enviado

    #capturar mensaje de error
   """ def test_validacion_cliente(self):
        with self.assertRaises(ValidationError) as qv:
            q = Cliente.objects.create(nombre="No permitido")
            q.full_clean()
        
        mensaje = dict(qv.exception)
        self.assertEqual(mensaje["nombre"][0], "No es una opcion permitida")
        """