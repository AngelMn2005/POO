<div align="center">

# 📝 Registro de Uso de Inteligencia Artificial
### Tarea de Programación Orientada a Objetos — Python
**IA utilizada:** Claude (Anthropic) | **URL:** [claude.ai](https://claude.ai)

</div>

---

> **Metodología aplicada:**
> Para cada ejercicio se siguió el ciclo:
> 1. Prompt de explicación → Entender el tema
> 2. Prompt de proceso similar → Pedir un ejercicio parecido para practicar
> 3. Resolución propia → Resolver sin copiar la respuesta
> 4. Repetición hasta comprender completamente

---

## 🟦 NIVEL PRINCIPIANTE

---

### 📦 BLOQUE 0 — Introducción a la POO

#### PREGUNTA 1 — Identificar 5 clases para un sistema de biblioteca

**Prompt de explicación:**
```
¿Qué es una clase en Programación Orientada a Objetos?
Explícame con un ejemplo sencillo cómo identificar clases
en un problema del mundo real, como un sistema de biblioteca.
```

**Prompt de proceso similar:**
```
Dame un ejercicio parecido: pídeme que identifique 5 clases
para modelar un sistema de hospital o tienda virtual,
sin darme la respuesta directamente.
```

**Proceso similar practicado (resolución propia):**
Para un sistema de hospital identifiqué: `Paciente`, `Doctor`, `Consulta`, `Medicamento`, `Factura`.

**Resultado aprendido:** Una clase representa cualquier "entidad" que tiene atributos (datos) y comportamiento (métodos) en el dominio del problema.

---

#### PREGUNTA 2 — Clase Persona con nombre y edad

**Prompt de explicación:**
```
¿Cómo se crea una clase en Python con el constructor __init__?
Muéstrame cómo crear la clase Persona con atributos nombre y edad,
e instanciar 3 objetos diferentes con datos distintos.
```

**Prompt de proceso similar:**
```
Ahora dime cómo crear una clase Vehículo con marca, modelo y año,
y pídeme que yo instancie 3 vehículos con datos inventados.
No me des la solución, solo el enunciado.
```

**Proceso similar practicado (resolución propia):**
```python
class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca  = marca
        self.modelo = modelo
        self.año    = año

v1 = Vehiculo("Toyota", "Corolla", 2020)
v2 = Vehiculo("Chevrolet", "Spark",  2019)
v3 = Vehiculo("Kia",      "Rio",    2022)
```

---

#### PREGUNTA 3 — Diferencia entre clase y objeto

**Prompt de explicación:**
```
Explícame con tus propias palabras, usando una analogía del mundo
real, cuál es la diferencia entre una clase y un objeto en Python.
```

**Prompt de proceso similar:**
```
Dame otro ejemplo de la vida diaria (diferente a molde/galleta)
que ilustre la diferencia entre clase y objeto, y luego pídeme
que yo dé mi propio ejemplo.
```

**Proceso similar practicado (resolución propia):**
- **Clase** → El plano arquitectónico de una casa (define cuartos, puertas, ventanas).
- **Objeto** → La casa construida en la calle Olmedo #123 (instancia específica del plano).

---

### 📦 BLOQUE 1 — Constructores y Validación

#### PREGUNTA 1 — Clase Producto con validación de precio

**Prompt de explicación:**
```
¿Cómo puedo validar los parámetros del constructor __init__ en Python?
Por ejemplo, si creo una clase Producto con precio, ¿cómo evito
que el precio sea negativo? Muéstrame con raise ValueError.
```

**Prompt de proceso similar:**
```
Dame un ejercicio similar: crear una clase Empleado con sueldo,
donde el sueldo no pueda ser menor al salario mínimo (400 dólares).
Pídeme que yo lo resuelva solo.
```

**Proceso similar practicado (resolución propia):**
```python
class Empleado:
    SALARIO_MINIMO = 400

    def __init__(self, nombre, sueldo):
        if sueldo < self.SALARIO_MINIMO:
            raise ValueError(f"El sueldo no puede ser menor a ${self.SALARIO_MINIMO}")
        self.nombre = nombre
        self.sueldo = sueldo
```

---

#### PREGUNTA 2 — @classmethod desde diccionario

**Prompt de explicación:**
```
¿Para qué sirve el decorador @classmethod en Python?
Muéstrame cómo usarlo en una clase Estudiante para crear
un objeto desde un diccionario con el método from_dict().
```

**Prompt de proceso similar:**
```
Dame un ejercicio parecido: crear una clase Libro con un
@classmethod llamado desde_tupla() que reciba (titulo, autor, paginas).
Pídeme que yo lo haga solo.
```

**Proceso similar practicado (resolución propia):**
```python
class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo  = titulo
        self.autor   = autor
        self.paginas = paginas

    @classmethod
    def desde_tupla(cls, datos):
        return cls(datos[0], datos[1], datos[2])

libro = Libro.desde_tupla(("Python Crash Course", "Eric Matthes", 544))
```

---

### 📦 BLOQUE 2 — Variables y Tipos de Datos

#### PREGUNTA 1 — Variables simples y complejas

**Prompt de explicación:**
```
¿Cuáles son los tipos de datos básicos en Python?
Explícame la diferencia entre tipos simples (str, int, float, bool)
y tipos complejos (list, dict, tuple, set) con ejemplos cortos.
```

**Prompt de proceso similar:**
```
Pídeme que yo declare al menos 2 variables de cada tipo
(simples y complejas) usando información de mi ciudad o carrera.
No me des la respuesta.
```

**Proceso similar practicado (resolución propia):**
```python
ciudad   = "Milagro"          # str
codigo   = 9          	      # int
latitud  = -2.1344            # float
activo   = True               # bool
materias = ["POO", "BD", "IA"]  # list
info     = {"universidad": "UNEMI", "año": 2024}  # dict
```

---

## 🟪 NIVEL INTERMEDIO

---

### 📦 BLOQUE 3 — Operadores

#### PREGUNTA 1 — Operadores aritméticos

**Prompt de explicación:**
```
Explícame todos los operadores aritméticos de Python:
+, -, *, /, %, **, //
¿Qué hace cada uno? Muéstrame con a=20 y b=4.
```

**Prompt de proceso similar:**
```
Dame un ejercicio donde yo use todos los operadores aritméticos
con variables a=15 y b=3, y pídeme que calcule cada resultado
a mano antes de ejecutarlo.
```

**Proceso similar practicado (resolución propia):**
```
a=15, b=3 → Suma=18, Resta=12, Mult=45, Div=5.0,
M�dulo=0, Potencia=3375, DivEntera=5
```

---

#### PREGUNTA 2 — Identidad: == vs is

**Prompt de explicación:**
```
¿Cuál es la diferencia entre == e is en Python?
¿Por qué dos listas con los mismos valores tienen == True pero is False?
Explícame el concepto de identidad vs igualdad de valor.
```

**Prompt de proceso similar:**
```
Dame un ejercicio donde yo compruebe el comportamiento de is vs ==
con strings y números pequeños (interning de Python), y que luego
lo explique con mis palabras.
```

**Proceso similar practicado (resolución propia):**
```python
a = "hola"
b = "hola"
# Strings cortos: a is b → True (Python los reutiliza en memoria)

x = [1, 2]
y = [1, 2]
# Listas:  x is y → False (son objetos distintos en memoria)
```

---

#### PREGUNTA 3 — Precedencia de operadores

**Prompt de explicación:**
```
¿Cuál es el orden de precedencia de los operadores en Python?
Explícame paso a paso cómo se evalúa esta expresión:
x = 2 + 1 * 2 % 2 + (2**1)//2
```

**Prompt de proceso similar:**
```
Dame una expresión similar con al menos 5 operadores distintos
y pídeme que la evalúe paso a paso antes de ejecutarla.
```

**Proceso similar practicado (resolución propia):**
```
y = 3 + 2**2 * 4 // 3 - 1
→ 2**2 = 4 → 4*4=16 → 16//3=5 → 3+5-1 = 7
```

---

### 📦 BLOQUE 4 — Entrada y Salida

#### PREGUNTA 1 — input() y f-string

**Prompt de explicación:**
```
¿Cómo funciona input() en Python para leer datos del usuario?
¿Cómo uso f-strings para mostrar variables dentro de un texto?
Muéstrame un ejemplo pidiendo nombre y edad.
```

**Prompt de proceso similar:**
```
Pídeme que haga un programa que solicite nombre, ciudad y carrera,
y muestre un mensaje completo usando f-string. Sin darme la solución.
```

**Proceso similar practicado (resolución propia):**
```python
nombre  = input("Nombre : ")
ciudad  = input("Ciudad : ")
carrera = input("Carrera: ")
print(f"Hola {nombre}, estudias {carrera} en {ciudad}.")
```

---

#### PREGUNTA 2 — Suma y Promedio de dos números

**Prompt de explicación:**
```
¿Cómo leo dos números del usuario y calculo su suma y promedio
en Python? ¿Qué validaciones debo agregar para que no falle
si el usuario escribe letras en lugar de números?
```

**Prompt de proceso similar:**
```
Dame un ejercicio similar: leer 3 notas del usuario, validarlas,
y calcular promedio y calificación letra. Pídeme que yo lo resuelva.
```

**Proceso similar practicado (resolución propia):**
```python
notas = []
for i in range(3):
    while True:
        try:
            n = float(input(f"Nota {i+1}: "))
            if 0 <= n <= 10:
                notas.append(n)
                break
        except ValueError:
            print("Error: ingrese un número.")
promedio = sum(notas) / len(notas)
```

---

### 📦 BLOQUE 5 — Condicionales

#### PREGUNTA 1 — Par o impar

**Prompt de explicación:**
```
¿Cómo determino si un número es par o impar en Python?
¿Qué operador uso y cómo estructuro el if/else?
```

**Prompt de proceso similar:**
```
Dame un ejercicio donde debo verificar si un número es divisible
entre 3 y entre 5 al mismo tiempo, usando operadores lógicos.
```

**Proceso similar practicado (resolución propia):**
```python
n = int(input("Número: "))
if n % 3 == 0 and n % 5 == 0:
    print("Divisible entre 3 y 5")
elif n % 3 == 0:
    print("Solo divisible entre 3")
elif n % 5 == 0:
    print("Solo divisible entre 5")
else:
    print("No es divisible entre 3 ni 5")
```

---

#### PREGUNTA 2 — Calificación letra

**Prompt de explicación:**
```
¿Cómo uso elif en Python para asignar una calificación en letra
(A, B, C, D, F) según una nota numérica del 0 al 100?
```

**Prompt de proceso similar:**
```
Dame un ejercicio similar: clasificar el IMC de una persona
en: bajo peso, normal, sobrepeso u obesidad, según rangos.
```

**Proceso similar practicado (resolución propia):**
```python
imc = float(input("IMC: "))
if   imc < 18.5: categoria = "Bajo peso"
elif imc < 25.0: categoria = "Normal"
elif imc < 30.0: categoria = "Sobrepeso"
else:            categoria = "Obesidad"
```

---

### 📦 BLOQUE 6 — Bucles

#### PREGUNTA 1 — while

**Prompt de explicación:**
```
¿Cómo funciona el bucle while en Python?
Muéstrame cómo imprimir los números del 1 al 10 usando while
y explícame cuándo es mejor usar while en vez de for.
```

**Prompt de proceso similar:**
```
Dame un ejercicio con while: pedir números al usuario hasta
que ingrese un número negativo, y mostrar el acumulado.
```

**Proceso similar practicado (resolución propia):**
```python
total = 0
while True:
    n = int(input("Número (negativo para salir): "))
    if n < 0:
        break
    total += n
print(f"Total acumulado: {total}")
```

---

#### PREGUNTA 2 — enumerate()

**Prompt de explicación:**
```
¿Para qué sirve enumerate() en Python?
Muéstrame cómo recorrer una lista mostrando el índice
y el valor de cada elemento.
```

**Prompt de proceso similar:**
```
Pídeme que recorra una lista de materias con enumerate()
y las muestre numeradas del 1 en adelante (no desde 0).
```

**Proceso similar practicado (resolución propia):**
```python
materias = ["POO", "Base de Datos", "Redes"]
for i, materia in enumerate(materias, start=1):
    print(f"{i}. {materia}")
```

---

#### PREGUNTA 3 — List Comprehension

**Prompt de explicación:**
```
¿Qué es una list comprehension en Python y cuándo usarla?
Muéstrame cómo generar la lista de cuadrados de los números
pares del 1 al 10 en una sola línea.
```

**Prompt de proceso similar:**
```
Dame un ejercicio similar: generar una lista de los cubos
de los números impares del 1 al 15.
```

**Proceso similar practicado (resolución propia):**
```python
cubos_impares = [n**3 for n in range(1, 16) if n % 2 != 0]
# → [1, 27, 125, 343, 729, 1331, 2197, 3375]
```

---

### 📦 BLOQUE 7 — Funciones

#### PREGUNTA 3 — Recursividad (factorial)

**Prompt de explicación:**
```
¿Qué es la recursividad en programación?
Explícame paso a paso cómo funciona el factorial recursivo
y cuál es el caso base que detiene la recursión.
```

**Prompt de proceso similar:**
```
Dame un ejercicio recursivo diferente: calcular la suma
de todos los números del 1 al n usando recursividad.
Pídeme que yo lo haga.
```

**Proceso similar practicado (resolución propia):**
```python
def suma_recursiva(n):
    if n <= 0:
        return 0
    return n + suma_recursiva(n - 1)

# suma_recursiva(5) = 5+4+3+2+1 = 15
```

---

### 📦 BLOQUE 9 — Tuplas

#### PREGUNTA 1 — Inmutabilidad

**Prompt de explicación:**
```
¿Por qué las tuplas son inmutables en Python?
¿Qué error ocurre si intento modificar un elemento de una tupla?
¿Cuándo es mejor usar tupla en lugar de lista?
```

**Prompt de proceso similar:**
```
Dame un ejercicio donde yo deba decidir entre usar lista o tupla
para almacenar: coordenadas GPS, lista de compras, días de la semana.
Explícame por qué en cada caso.
```

**Proceso similar practicado (resolución propia):**
- `coordenadas = (-2.13, -79.58)` → **tupla** (no cambian)
- `compras = ["leche", "pan"]` → **lista** (se modifican)
- `dias = ("lun","mar","mié","jue","vie","sáb","dom")` → **tupla**

---

### 📦 BLOQUE 11 — Conjuntos (Sets)

#### PREGUNTA 1 — Operaciones de conjuntos

**Prompt de explicación:**
```
¿Qué es un set en Python y para qué sirve?
Explícame las operaciones unión (|), intersección (&)
y diferencia (-) con un ejemplo numérico.
```

**Prompt de proceso similar:**
```
Dame un ejercicio con conjuntos: tengo la lista de estudiantes
que aprobaron el primer parcial y la del segundo parcial.
Pídeme que encuentre quiénes aprobaron ambos, solo uno, y ninguno.
```

**Proceso similar practicado (resolución propia):**
```python
parcial1 = {"Ana", "Luis", "Pedro", "Maria"}
parcial2 = {"Luis", "Maria", "Sofia", "Juan"}

ambos    = parcial1 & parcial2   # {"Luis", "Maria"}
solo_p1  = parcial1 - parcial2   # {"Ana", "Pedro"}
solo_p2  = parcial2 - parcial1   # {"Sofia", "Juan"}
```

---

## 🟩 NIVEL AVANZADO

---

### 📦 BLOQUE 12 — Manejo de Excepciones

#### PREGUNTA 1 — ValueError

**Prompt de explicación:**
```
¿Qué es el manejo de excepciones en Python?
¿Cómo uso try/except para capturar un ValueError
cuando el usuario ingresa texto en vez de número?
```

**Prompt de proceso similar:**
```
Dame un ejercicio donde el usuario ingresa su año de nacimiento
y debo calcular su edad. Pídeme que maneje el ValueError
si escribe algo que no sea número, y que valide que el año sea razonable.
```

**Proceso similar practicado (resolución propia):**
```python
try:
    año = int(input("Año de nacimiento: "))
    if año < 1900 or año > 2024:
        raise ValueError("Año fuera de rango")
    edad = 2024 - año
    print(f"Tienes aproximadamente {edad} años.")
except ValueError as e:
    print(f"Error: {e}")
```

---

#### PREGUNTA 3 — ZeroDivisionError

**Prompt de explicación:**
```
¿Cómo capturo múltiples tipos de excepciones en un solo bloque try?
Explícame con un ejemplo de división donde puede ocurrir
ValueError (entrada no numérica) y ZeroDivisionError (dividir por 0).
```

**Prompt de proceso similar:**
```
Dame un ejercicio donde el usuario ingresa el numerador y denominador
de una fracción, y debo manejar ambos errores con except separados
y mostrar mensajes diferentes para cada caso.
```

**Proceso similar practicado (resolución propia):**
```python
try:
    num = int(input("Numerador  : "))
    den = int(input("Denominador: "))
    resultado = num / den
    print(f"Resultado: {resultado}")
except ValueError:
    print("Error: ingrese solo números enteros.")
except ZeroDivisionError:
    print("Error: el denominador no puede ser cero.")
```

---

### 📦 BLOQUE 13 — Decoradores

#### PREGUNTA 1 — @iniciar

**Prompt de explicación:**
```
¿Qué es un decorador en Python y cómo funciona internamente?
Muéstrame cómo crear un decorador llamado "iniciar" que imprima
"Iniciando..." antes de ejecutar cualquier función.
```

**Prompt de proceso similar:**
```
Dame un ejercicio donde yo cree un decorador llamado "finalizar"
que imprima "Proceso terminado." después de ejecutar la función.
```

**Proceso similar practicado (resolución propia):**
```python
def finalizar(func):
    def wrapper(*args, **kwargs):
        resultado = func(*args, **kwargs)
        print("Proceso terminado.")
        return resultado
    return wrapper

@finalizar
def guardar_datos():
    print("Guardando datos...")

guardar_datos()
# → Guardando datos...
# → Proceso terminado.
```

---

#### PREGUNTA 3 — @log

**Prompt de explicación:**
```
¿Cómo creo un decorador @log que registre el nombre de la función,
sus argumentos y el resultado que retorna?
Muéstrame con la función suma(a, b).
```

**Prompt de proceso similar:**
```
Pídeme que cree un decorador @cronometrar que mida cuánto tarda
en ejecutarse una función usando el módulo time.
```

**Proceso similar practicado (resolución propia):**
```python
import time

def cronometrar(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"Tiempo: {fin - inicio:.4f}s")
        return resultado
    return wrapper

@cronometrar
def operacion_lenta():
    time.sleep(0.5)

operacion_lenta()  # → Tiempo: 0.5001s
```

---

### 📦 BLOQUE 14 — Unpacking Avanzado

#### PREGUNTA 1 — *mitad

**Prompt de explicación:**
```
¿Cómo funciona el unpacking extendido en Python con el operador *?
Muéstrame cómo desempaquetar (10, 20, 30, 40) en primera, *mitad, ultima.
```

**Prompt de proceso similar:**
```
Dame un ejercicio donde desempaquete una lista de 6 números:
el primero, los 4 del medio y el último, en variables separadas.
```

**Proceso similar practicado (resolución propia):**
```python
datos = [5, 10, 15, 20, 25, 30]
primero, *centro, ultimo = datos
# primero=5, centro=[10,15,20,25], ultimo=30
```

---

### 📦 BLOQUE 15 — Programación Funcional

#### PREGUNTA 1 — map()

**Prompt de explicación:**
```
¿Para qué sirve map() en Python?
Muéstrame cómo usar map() con una lambda para aplicar
una operación a todos los elementos de una lista.
```

**Prompt de proceso similar:**
```
Dame un ejercicio donde use map() para convertir una lista de
temperaturas en Celsius a Fahrenheit: [0, 20, 37, 100].
```

**Proceso similar practicado (resolución propia):**
```python
celsius     = [0, 20, 37, 100]
fahrenheit  = list(map(lambda c: (c * 9/5) + 32, celsius))
# → [32.0, 68.0, 98.6, 212.0]
```

---

#### PREGUNTA 3 — reduce()

**Prompt de explicación:**
```
¿Cómo funciona reduce() de functools en Python?
Muéstrame cómo usarlo para multiplicar todos los elementos
de una lista paso a paso.
```

**Prompt de proceso similar:**
```
Dame un ejercicio donde use reduce() para encontrar el máximo
de una lista sin usar max(). Pídeme que lo haga solo.
```

**Proceso similar practicado (resolución propia):**
```python
from functools import reduce

numeros = [3, 7, 2, 9, 4]
maximo  = reduce(lambda a, b: a if a > b else b, numeros)
# → 9
```

---

### 📦 BLOQUE 16 — Persistencia

#### PREGUNTA 2 — JSON

**Prompt de explicación:**
```
¿Cómo guardo y cargo datos en formato JSON en Python?
Muéstrame el uso de json.dump() y json.load() con un ejemplo
de guardar un diccionario y volver a leerlo.
```

**Prompt de proceso similar:**
```
Dame un ejercicio donde yo guarde una lista de 3 productos
(con nombre y precio) en un archivo JSON, luego lo cargue
y muestre solo los que cuestan más de $50.
```

**Proceso similar practicado (resolución propia):**
```python
import json

productos = [
    {"nombre": "Laptop", "precio": 900},
    {"nombre": "Mouse",  "precio": 25},
    {"nombre": "Monitor","precio": 350},
]

with open("productos.json", "w") as f:
    json.dump(productos, f, indent=4)

with open("productos.json", "r") as f:
    data = json.load(f)

caros = [p for p in data if p["precio"] > 50]
for p in caros:
    print(f"{p['nombre']}: ${p['precio']}")
```

---

### 📦 BLOQUE 17 — Proyecto Integrador

#### Uso de Mixins

**Prompt de explicación:**
```
¿Qué son los Mixins en Python y cómo se usan con herencia múltiple?
Muéstrame cómo crear una clase que herede de PromedioMixin
y ValidationMixin al mismo tiempo, y use métodos de ambas.
```

**Prompt de proceso similar:**
```
Dame un ejercicio donde yo cree una clase Empleado que use
un SueldoMixin (calcular bono) y un ValidacionMixin (validar email),
y los combine en una sola clase. Pídeme que lo resuelva solo.
```

**Proceso similar practicado (resolución propia):**
```python
class SueldoMixin:
    def calcular_bono(self, sueldo, porcentaje=0.10):
        return sueldo * porcentaje

class ValidacionMixin:
    def validar_email(self, correo):
        return "@" in correo and ".com" in correo

class Empleado(SueldoMixin, ValidacionMixin):
    def __init__(self, nombre, correo, sueldo):
        self.nombre = nombre
        self.correo = correo
        self.sueldo = sueldo

    def info(self):
        email_ok = self.validar_email(self.correo)
        bono     = self.calcular_bono(self.sueldo)
        print(f"{self.nombre} | Email válido: {email_ok} | Bono: ${bono:.2f}")
```

---

## 📊 Resumen de Prompts Utilizados

| Bloque | Tema | Prompts usados |
|--------|------|---------------|
| BLOQUE_0 | POO | 6 prompts |
| BLOQUE_1 | Constructores | 4 prompts |
| BLOQUE_2 | Variables | 2 prompts |
| BLOQUE_3 | Operadores | 6 prompts |
| BLOQUE_4 | E/S | 4 prompts |
| BLOQUE_5 | Condicionales | 4 prompts |
| BLOQUE_6 | Bucles | 6 prompts |
| BLOQUE_7 | Funciones | 2 prompts |
| BLOQUE_9 | Tuplas | 2 prompts |
| BLOQUE_11 | Sets | 2 prompts |
| BLOQUE_12 | Excepciones | 4 prompts |
| BLOQUE_13 | Decoradores | 4 prompts |
| BLOQUE_14 | Unpacking | 2 prompts |
| BLOQUE_15 | Funcional | 4 prompts |
| BLOQUE_16 | Persistencia | 2 prompts |
| BLOQUE_17 | Mixins | 2 prompts |
| **TOTAL** | | **56 prompts** |

---

<div align="center">

**IA utilizada:** Claude (Anthropic) — [claude.ai](https://claude.ai)
*Usada como herramienta de aprendizaje, no para copiar respuestas.*

</div>
