import json
class ValidationMixin:
    @staticmethod
    def validar_vacio(valor):
        # Valida que el campo no esté vacío
        return bool(valor.strip())
    @staticmethod
    def normalizar_texto(texto):
        # Limpia espacios y pone formato correcto
        return texto.strip().title()
    @staticmethod
    def validar_solo_letras(nombre):
        # Valida que el texto tenga solo letras
        return all(parte.isalpha() for parte in nombre.split())
    @staticmethod
    def validar_numero_positivo(valor):
        try:
            valor = float(valor)
            return valor > 0
        except ValueError:
            return False
    @staticmethod
    def validar_porcentaje(valor):
        try:
            valor = float(valor)
            return 0 <= valor <= 100
        except ValueError:
            return False
    @staticmethod
    def validar_nota(nota):
        try:
            nota = float(nota)
            return 0 <= nota <= 10
        except ValueError:
            return False
    @staticmethod
    def validar_altura(valor):
        try:
            valor = float(valor)
            return 0 < valor <= 3
        except ValueError:
            return False
        
class IMCMixin:
    @staticmethod
    def calcular_imc(peso, altura):

        return round(peso / (altura ** 2),2)
    @staticmethod
    def clasificar(imc):
        if imc < 18.5:
            return "Bajo peso"
        elif imc < 25:
            return "Normal"
        elif imc < 30:
            return "Sobrepeso"
        else:
            return "Obesidad"
        
class TemperaturaMixin:
    @staticmethod
    def a_fahrenheit(celsius):
        return round((celsius * 9 / 5) + 32, 2)
    @staticmethod
    def a_kelvin(celsius):

        return round(celsius + 273.15, 2)
    @staticmethod
    def validar_temperatura(valor):
        try:
            float(valor)
            return True
        except ValueError:
            return False
        
    
    
class PromedioMixin:
    @staticmethod
    def calcular_promedio(notas):
        if not notas:
            return 0
        return round(sum(notas) / len(notas), 2)
    @staticmethod
    def calcular_max( notas):

        return max(notas)
    @staticmethod
    def calcular_min(notas):

        return min(notas)
    
    
class ValidacionUsuarioMixin:
    @staticmethod
    def validar_email(correo):
        return "@" in correo and ".com" in correo

    @staticmethod
    def validar_edad(edad):
        return edad >= 18
    
    
    
class ExportarMixin:

    @staticmethod
    def exportar_json(datos):

        return json.dumps(
            datos,
            indent=4,
            ensure_ascii=False
        )
    @staticmethod
    def exportar_csv(datos):

        resultado = ""
        for item in datos:
            fila = ",".join(
                str(valor)
                for valor in item.values()
            )
            resultado += fila + "\n"
        return resultado

class DescuentoMixin:
    @staticmethod
    def calcular_descuento(precio, porcentaje):

        return round(
            precio - (precio * porcentaje / 100),
            2
        )