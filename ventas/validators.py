from django.core.exceptions import ValidationError
import re

def validar_par(value):
    if value % 2 != 0:
        # format string
        #raise ValidationError("El número no es par")
        #raise ValidationError("%(value)s no es un numero par")
        #raise ValidationError("%s no es un numero par", %value)#en esta posicion: %s  coloca el valor
        #raise ValidationError("%s no %s es un numero par", %(value,value))#envia  valores a dos posiciones
        
        raise ValidationError("%(value2)s no es un numero par", params={"value2": value})

def  validation_cliente(value):
    if value == "No permitido":
        raise ValidationError("No se una opción permitida")

def validar_poliza(value):
    #Validar el numero de poliza con 7 caractere
    num_pattern = r"^[A-Z0-9]{7}$"

    if not re.match(num_pattern, value):
        raise ValidationError("El número de póliza %(value2)s no es válido. Asegúrate de que tenga 7 caracteres alfanuméricos.", params={"value2": value})


def validar_precio(value):
    #Valida que el precio sea mayor a cero.
    if value <= 0:
        raise ValidationError("El precio debe ser un valor positivo. Ingresaste:%(value2)s", params={"value2": value})


