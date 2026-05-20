<div align="center">

# 📝 Registro de Uso de Inteligencia Artificial
### Tarea POO — Python | IA: Claude (Anthropic)

</div>

> **Metodología:** Para cada ejercicio → Prompt de explicación → Prompt de proceso similar → Resolución propia → Repetir hasta comprender.

---

## 🟦 NIVEL PRINCIPIANTE

---

### BLOQUE 0 — Introducción a la POO

---

#### Pregunta 1 — Identificar 5 clases para un sistema de biblioteca

**Prompt de explicación usado:**
```
¿Qué es una clase en Programación Orientada a Objetos?
Explícame cómo identificar clases en un sistema de biblioteca
con un ejemplo sencillo del mundo real.
```

**Prompt de proceso similar:**
```
Dame un ejercicio parecido: dime que identifique 5 clases
para un sistema de hospital. No me des la respuesta, solo el enunciado.
```

**Mi resolución del proceso similar:**
```
Sistema Hospital:
1. Paciente   → datos del paciente
2. Doctor     → médico que atiende
3. Consulta   → cita médica
4. Medicamento → fármacos recetados
5. Factura    → cobro del servicio
```

**Lo que aprendí:** Una clase representa cualquier entidad del mundo real que tiene datos (atributos) y comportamiento (métodos).

---

#### Pregunta 2 — Clase Persona con nombre y edad

**Prompt de explicación usado:**
```
¿Cómo se crea una clase en Python con el constructor __init__?
Muéstrame cómo crear la clase Persona con atributos nombre y edad
e instanciar 3 objetos con datos diferentes.
```

**Prompt de proceso similar:**
```
Pídeme que yo cree una clase Vehiculo con marca, modelo y año,
e instancie 3 vehículos con datos inventados. Sin darme la solución.
```

**Mi resolución del proceso similar:**
```python
class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self.marca  = marca
        self.modelo = modelo
        self.anio   = anio

v1 = Vehiculo("Toyota",    "Corolla", 2020)
v2 = Vehiculo("Chevrolet", "Spark",   2019)
v3 = Vehiculo("Kia",       "Rio",     2022)
```

**Lo que aprendí:** El constructor `__init__` se ejecuta automáticamente al crear el objeto. `self` referencia al objeto actual.

---

#### Pregunta 3 — Diferencia entre clase y objeto

**Prompt de explicación usado:**
```
Explícame con una analogía del mundo real la diferencia
entre clase y objeto en Python.
```

**Prompt de proceso similar:**
```
Dame otro ejemplo de la vida diaria que ilustre la diferencia
entre clase y objeto, y luego pídeme que yo dé mi propio ejemplo.
```

**Mi resolución del proceso similar:**
```
Clase  → El plano de una casa (define cuartos, puertas, ventanas)
Objeto → La casa construida en la calle Olmedo #123

Clase  → La receta de una torta (ingredientes y pasos)
Objeto → La torta de chocolate que hornee el martes
```

---

### BLOQUE 1 — Constructores y Validación

---

#### Pregunta 1 — Clase Producto con validación de precio

**Prompt de explicación usado:**
```
¿Cómo puedo validar parámetros en el constructor __init__ de Python?
Si creo una clase Producto con precio, ¿cómo evito que el precio
sea negativo usando raise ValueError?
```

**Prompt de proceso similar:**
```
Pídeme que cree una clase Empleado donde el sueldo no pueda ser
menor al salario mínimo de $400. Sin darme la solución.
```

**Mi resolución del proceso similar:**
```python
class Empleado:
    SALARIO_MINIMO = 400

    def __init__(self, nombre, sueldo):
        if sueldo < self.SALARIO_MINIMO:
            raise ValueError(f"Sueldo no puede ser menor a ${self.SALARIO_MINIMO}")
        self.nombre = nombre
        self.sueldo = sueldo
```

**Lo que aprendí:** `raise ValueError("mensaje")` lanza una excepción desde el constructor para rechazar datos inválidos antes de crear el objeto.

---

#### Pregunta 2 — @classmethod desde diccionario

**Prompt de explicación usado:**
```
¿Para qué sirve el decorador @classmethod en Python?
Muéstrame cómo usarlo en una clase Estudiante para crear
un objeto desde un diccionario con el método from_dict().
```

**Prompt de proceso similar:**
```
Pídeme que cree una clase Libro con un @classmethod llamado
desde_tupla() que reciba (titulo, autor, paginas). Sin darme la solución.
```

**Mi resolución del proceso similar:**
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

**Lo que aprendí:** `@classmethod` recibe `cls` en lugar de `self` y puede crear instancias alternativas sin llamar `__init__` directamente.

---

### BLOQUE 2 — Variables y Tipos de Datos

---

#### Pregunta 1 — Tipos simples y complejos

**Prompt de explicación usado:**
```
¿Cuáles son los tipos de datos básicos en Python?
Explícame la diferencia entre simples (str, int, float, bool)
y complejos (list, dict, tuple, set) con ejemplos cortos.
```

**Prompt de proceso similar:**
```
Pídeme que declare al menos 2 variables de cada tipo usando
información de mi ciudad o carrera. Sin darme la respuesta.
```

**Mi resolución del proceso similar:**
```python
# Simples
ciudad   = "Milagro"        # str
codigo   = 9                # int
latitud  = -2.1344          # float
activo   = True             # bool

# Complejos
materias = ["POO", "BD", "IA"]                   # list
info     = {"uni": "UNEMI", "año": 2024}         # dict
coordenadas = (-2.13, -79.58)                    # tuple
colores  = {"azul", "rojo", "verde"}             # set
```

---

#### Pregunta 2 — Indexación y slicing

**Prompt de explicación usado:**
```
¿Cómo accedo al primer y último elemento de una lista en Python?
¿Qué es el slicing y cómo funciona lista[1:4]?
```

**Prompt de proceso similar:**
```
Dame un ejercicio donde yo acceda al segundo elemento, al penúltimo
y haga un slice de los últimos 3 elementos de una lista de 7 items.
```

**Mi resolución del proceso similar:**
```python
nums = [10, 20, 30, 40, 50, 60, 70]
print(nums[1])      # 20  — segundo
print(nums[-2])     # 60  — penúltimo
print(nums[-3:])    # [50, 60, 70] — últimos 3
```

---

## 🟪 NIVEL INTERMEDIO

---

### BLOQUE 3 — Operadores

---

#### Pregunta 1 — Operadores aritméticos

**Prompt de explicación usado:**
```
Explícame todos los operadores aritméticos de Python:
+, -, *, /, %, **, //
¿Qué hace cada uno? Muéstrame con a=20 y b=4.
```

**Prompt de proceso similar:**
```
Dame un ejercicio donde yo calcule con a=15 y b=3
todos los operadores aritméticos a mano antes de ejecutarlo.
```

**Mi resolución del proceso similar:**
```
a=15, b=3
Suma            → 18
Resta           → 12
Multiplicación  → 45
División        → 5.0
Módulo          → 0
Potencia        → 3375
División Entera → 5
```

---

#### Pregunta 2 — Identidad vs Igualdad (== vs is)

**Prompt de explicación usado:**
```
¿Cuál es la diferencia entre == e is en Python?
¿Por qué dos listas con los mismos valores tienen == True pero is False?
Explícame identidad vs igualdad de valor.
```

**Prompt de proceso similar:**
```
Dame un ejercicio donde yo compare el comportamiento de is vs ==
con strings y listas, y que luego lo explique con mis palabras.
```

**Mi resolución del proceso similar:**
```python
a = "hola"
b = "hola"
print(a == b)   # True  — mismo valor
print(a is b)   # True  — Python reutiliza strings cortos en memoria

x = [1, 2]
y = [1, 2]
print(x == y)   # True  — mismos valores
print(x is y)   # False — son objetos distintos en memoria

# Conclusión: == compara valores, is compara identidad (dirección de memoria)
```

---

#### Pregunta 3 — Precedencia de operadores

**Prompt de explicación usado:**
```
¿Cuál es el orden de precedencia de operadores en Python?
Evalúa paso a paso: x = 2 + 1 * 2 % 2 + (2**1)//2
```

**Prompt de proceso similar:**
```
Dame una expresión con al menos 5 operadores distintos
y pídeme que la evalúe paso a paso antes de ejecutarla.
```

**Mi resolución del proceso similar:**
```
y = 3 + 2**2 * 4 // 3 - 1

Paso 1: 2**2  = 4       → potencia primero
Paso 2: 4 * 4 = 16      → multiplicación
Paso 3: 16//3 = 5       → división entera
Paso 4: 3+5-1 = 7       → suma y resta de izquierda a derecha

y = 7  ✔
```

---

### BLOQUE 4 — Entrada y Salida

---

#### Pregunta 1 — input() y f-string

**Prompt de explicación usado:**
```
¿Cómo funciona input() en Python para leer datos del usuario?
¿Cómo uso f-strings para mostrar variables dentro de un texto?
Muéstrame pidiendo nombre y edad con validaciones.
```

**Prompt de proceso similar:**
```
Pídeme hacer un programa que solicite nombre, ciudad y carrera,
y muestre un mensaje completo con f-string. Sin darme la solución.
```

**Mi resolución del proceso similar:**
```python
nombre  = input("Nombre : ").strip().title()
ciudad  = input("Ciudad : ").strip().title()
carrera = input("Carrera: ").strip()
print(f"Hola {nombre}, estudias {carrera} en {ciudad}.")
```

---

#### Pregunta 2 — Suma y Promedio

**Prompt de explicación usado:**
```
¿Cómo leo dos números del usuario y calculo suma y promedio?
¿Qué validaciones debo agregar para que no falle si el usuario
escribe letras en lugar de números?
```

**Prompt de proceso similar:**
```
Pídeme leer 3 notas, validarlas y calcular promedio y calificación letra.
```

**Mi resolución del proceso similar:**
```python
notas = []
for i in range(3):
    while True:
        try:
            n = float(input(f"Nota {i+1}: "))
            if 0 <= n <= 10:
                notas.append(n)
                break
            print("La nota debe estar entre 0 y 10.")
        except ValueError:
            print("Error: ingrese un número.")

promedio = sum(notas) / len(notas)
letra = "A" if promedio >= 9 else "B" if promedio >= 7 else "C"
print(f"Promedio: {promedio:.1f} — Calificación: {letra}")
```

---

#### Pregunta 3 — Conversión Celsius a Fahrenheit

**Prompt de explicación usado:**
```
¿Cómo convierto Celsius a Fahrenheit en Python?
Muéstrame la fórmula y cómo validar que la entrada sea numérica.
```

**Prompt de proceso similar:**
```
Pídeme convertir Fahrenheit a Celsius con la fórmula correcta
y con validación de entrada numérica.
```

**Mi resolución del proceso similar:**
```python
while True:
    try:
        f = float(input("Fahrenheit: "))
        break
    except ValueError:
        print("Ingrese un número válido.")

c = (f - 32) * 5/9
print(f"{f}°F = {c:.2f}°C")
```

---

### BLOQUE 5 — Condicionales

---

#### Pregunta 1 — Par o Impar

**Prompt de explicación usado:**
```
¿Cómo determino si un número es par o impar en Python?
¿Qué operador uso y cómo estructuro el if/else?
```

**Prompt de proceso similar:**
```
Dame un ejercicio donde yo verifique si un número es divisible
entre 3 y entre 5 al mismo tiempo con operadores lógicos.
```

**Mi resolución del proceso similar:**
```python
n = int(input("Número: "))
if n % 3 == 0 and n % 5 == 0:
    print("Divisible entre 3 y 5 (FizzBuzz)")
elif n % 3 == 0:
    print("Solo divisible entre 3")
elif n % 5 == 0:
    print("Solo divisible entre 5")
else:
    print("No es divisible entre 3 ni 5")
```

---

#### Pregunta 2 — Calificación Letra

**Prompt de explicación usado:**
```
¿Cómo uso elif en Python para asignar calificación en letra
(A, B, C, D, F) según una nota numérica del 0 al 100?
```

**Prompt de proceso similar:**
```
Pídeme clasificar el IMC: bajo peso (<18.5), normal (18.5-25),
sobrepeso (25-30), obesidad (>30).
```

**Mi resolución del proceso similar:**
```python
imc = float(input("IMC: "))
if   imc < 18.5: print("Bajo peso")
elif imc < 25.0: print("Normal")
elif imc < 30.0: print("Sobrepeso")
else:            print("Obesidad")
```

---

#### Pregunta 3 — Calculadora con validación de operador

**Prompt de explicación usado:**
```
¿Cómo valido que el usuario ingrese un operador válido (+,-,*,/) en Python?
¿Cómo manejo la división por cero en una calculadora simple?
```

**Prompt de proceso similar:**
```
Pídeme hacer una calculadora que solo acepte los operadores +, -, *, /
y que maneje ZeroDivisionError si el usuario divide entre cero.
```

**Mi resolución del proceso similar:**
```python
a  = float(input("Número 1 : "))
b  = float(input("Número 2 : "))
op = input("Operador : ")

if op not in ["+", "-", "*", "/"]:
    print("Operador inválido")
elif op == "/" and b == 0:
    print("No se puede dividir entre cero")
else:
    ops = {"+": a+b, "-": a-b, "*": a*b, "/": a/b}
    print(f"Resultado: {ops[op]}")
```

---

### BLOQUE 6 — Bucles

---

#### Pregunta 1 — while

**Prompt de explicación usado:**
```
¿Cómo funciona el bucle while en Python?
Muéstrame cómo imprimir los números del 1 al 10 y cuándo
es mejor while en vez de for.
```

**Prompt de proceso similar:**
```
Pídeme hacer un programa con while que acumule números del usuario
hasta que ingrese un negativo, y muestre el total.
```

**Mi resolución del proceso similar:**
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

#### Pregunta 2 — enumerate()

**Prompt de explicación usado:**
```
¿Para qué sirve enumerate() en Python?
Muéstrame cómo recorrer una lista mostrando el índice y el valor.
```

**Prompt de proceso similar:**
```
Pídeme que recorra una lista de materias con enumerate()
numerándolas desde 1, no desde 0.
```

**Mi resolución del proceso similar:**
```python
materias = ["POO", "Base de Datos", "Redes", "IA"]
for i, materia in enumerate(materias, start=1):
    print(f"{i}. {materia}")

# 1. POO
# 2. Base de Datos
# 3. Redes
# 4. IA
```

---

#### Pregunta 3 — List Comprehension

**Prompt de explicación usado:**
```
¿Qué es una list comprehension en Python y cuándo usarla?
Muéstrame cómo generar cuadrados de pares del 1 al 10 en una línea.
```

**Prompt de proceso similar:**
```
Pídeme generar una lista de cubos de números impares del 1 al 15.
```

**Mi resolución del proceso similar:**
```python
cubos_impares = [n**3 for n in range(1, 16) if n % 2 != 0]
# → [1, 27, 125, 343, 729, 1331, 2197, 3375]
```

---

### BLOQUE 7 — Funciones

---

#### Pregunta 2 — *args

**Prompt de explicación usado:**
```
¿Qué es *args en Python y cómo funciona?
Muéstrame cómo crear una función que sume cualquier cantidad de números.
```

**Prompt de proceso similar:**
```
Pídeme crear una función con *args que calcule el promedio
de cualquier cantidad de números que le pase.
```

**Mi resolución del proceso similar:**
```python
def promedio(*args):
    if not args:
        return 0
    return sum(args) / len(args)

print(promedio(10, 20, 30))       # 20.0
print(promedio(5, 7, 9, 11, 13)) # 9.0
```

---

#### Pregunta 3 — Recursividad

**Prompt de explicación usado:**
```
¿Qué es la recursividad? Explícame paso a paso el factorial recursivo
y cuál es el caso base que detiene la recursión.
```

**Prompt de proceso similar:**
```
Dame un ejercicio recursivo diferente: calcular la suma
de todos los números del 1 al n. Sin darme la solución.
```

**Mi resolución del proceso similar:**
```python
def suma_recursiva(n):
    if n <= 0:           # caso base
        return 0
    return n + suma_recursiva(n - 1)

# suma_recursiva(5) → 5 + 4 + 3 + 2 + 1 + 0 = 15
```

---

### BLOQUE 8 — Listas

---

#### Pregunta 3 — Mayor y menor sin max()/min()

**Prompt de explicación usado:**
```
¿Cómo encuentro el mayor y el menor de una lista en Python
sin usar las funciones built-in max() y min()?
```

**Prompt de proceso similar:**
```
Pídeme encontrar el segundo mayor de una lista sin usar sorted()
ni max(). Que yo resuelva el algoritmo.
```

**Mi resolución del proceso similar:**
```python
nums = [34, 7, 23, 64, 2, 88, 15]
mayor = menor = nums[0]
for n in nums:
    if n > mayor: mayor = n
    if n < menor: menor = n

# Segundo mayor: ordenar mentalmente y tomar el penúltimo
segundo = float('-inf')
for n in nums:
    if n > segundo and n < mayor:
        segundo = n

print(f"Mayor: {mayor}, Segundo mayor: {segundo}")  # 88, 64
```

---

### BLOQUE 9 — Tuplas

---

#### Pregunta 1 — Inmutabilidad

**Prompt de explicación usado:**
```
¿Por qué las tuplas son inmutables en Python?
¿Qué error lanza Python si intento modificar un elemento?
¿Cuándo es mejor usar tupla en lugar de lista?
```

**Prompt de proceso similar:**
```
Dame un ejercicio donde yo deba decidir entre lista o tupla para:
coordenadas GPS, lista de compras, días de la semana. Que yo explique por qué.
```

**Mi resolución del proceso similar:**
```python
# Tupla → datos que NO deben cambiar
coordenadas = (-2.1344, -79.5862)   # latitud y longitud fijos
dias_semana = ("lun","mar","mié","jue","vie","sáb","dom")

# Lista → datos que SÍ cambian
compras = ["leche", "pan", "huevos"]
compras.append("mantequilla")   # ✓ permitido

# Si intentara: coordenadas[0] = 0  → TypeError ✗
```

---

### BLOQUE 10 — Diccionarios

---

#### Pregunta 3 — Referencia vs Copia

**Prompt de explicación usado:**
```
¿Qué pasa en Python si hago copia = datos siendo datos un diccionario,
y luego agrego copia["b"] = 2? ¿Qué le pasa a datos?
```

**Prompt de proceso similar:**
```
Pídeme demostrar la diferencia entre copia superficial (.copy())
y copia profunda (deepcopy) con un diccionario anidado.
```

**Mi resolución del proceso similar:**
```python
import copy

original = {"a": [1, 2, 3]}

# Copia superficial: listas internas aún se comparten
sup = original.copy()
sup["a"].append(99)
print(original)  # {"a": [1, 2, 3, 99]} — también cambió!

# Copia profunda: completamente independiente
prof = copy.deepcopy(original)
prof["a"].append(999)
print(original)  # {"a": [1, 2, 3, 99]} — no cambió ✓
```

---

### BLOQUE 11 — Conjuntos (Sets)

---

#### Pregunta 1 — Operaciones de conjuntos

**Prompt de explicación usado:**
```
¿Qué es un set en Python y para qué sirve?
Explícame las operaciones unión (|), intersección (&)
y diferencia (-) con un ejemplo numérico.
```

**Prompt de proceso similar:**
```
Dame un ejercicio con sets: estudiantes que aprobaron parcial 1
y parcial 2. Que yo encuentre quiénes aprobaron ambos, solo uno y ninguno.
```

**Mi resolución del proceso similar:**
```python
parcial1 = {"Ana", "Luis", "Pedro", "Maria"}
parcial2 = {"Luis", "Maria", "Sofia", "Juan"}

ambos    = parcial1 & parcial2   # {"Luis", "Maria"}
solo_p1  = parcial1 - parcial2   # {"Ana", "Pedro"}
solo_p2  = parcial2 - parcial1   # {"Sofia", "Juan"}
ninguno  = set()                 # nadie faltó a ambos en este caso
```

---

## 🟩 NIVEL AVANZADO

---

### BLOQUE 12 — Manejo de Excepciones

---

#### Pregunta 1 — ValueError

**Prompt de explicación usado:**
```
¿Qué es el manejo de excepciones en Python?
¿Cómo uso try/except para capturar un ValueError
cuando el usuario escribe texto en lugar de número?
```

**Prompt de proceso similar:**
```
Pídeme un programa que lea el año de nacimiento del usuario,
maneje el ValueError si escribe letras, y valide que el año sea razonable.
```

**Mi resolución del proceso similar:**
```python
while True:
    try:
        anio = int(input("Año de nacimiento: "))
        if anio < 1900 or anio > 2026:
            raise ValueError("Año fuera de rango válido")
        edad = 2026 - anio
        print(f"Tienes aproximadamente {edad} años.")
        break
    except ValueError as e:
        print(f"Error: {e}")
```

---

#### Pregunta 2 — IndexError

**Prompt de explicación usado:**
```
¿Cómo capturo un IndexError en Python al acceder a una posición
inválida en una lista? Muéstrame el patrón try/except.
```

**Prompt de proceso similar:**
```
Pídeme hacer un programa que pida al usuario una posición
de una lista y maneje tanto el IndexError como el ValueError
si el usuario escribe algo que no sea número.
```

**Mi resolución del proceso similar:**
```python
frutas = ["manzana", "banana", "pera", "uva"]
while True:
    try:
        pos = int(input(f"Posición (0-{len(frutas)-1}): "))
        print(f"Fruta: {frutas[pos]}")
        break
    except ValueError:
        print("Error: ingrese un número entero.")
    except IndexError:
        print(f"Error: posición fuera de rango (0-{len(frutas)-1}).")
```

---

#### Pregunta 3 — ValueError + ZeroDivisionError

**Prompt de explicación usado:**
```
¿Cómo capturo múltiples tipos de excepciones en un solo try?
Muéstrame con una división donde puede ocurrir ValueError
si el usuario escribe letras, y ZeroDivisionError si divide entre 0.
```

**Prompt de proceso similar:**
```
Pídeme hacer una calculadora de fracciones (numerador/denominador)
que maneje ambos errores con mensajes distintos para cada caso.
```

**Mi resolución del proceso similar:**
```python
while True:
    try:
        num = int(input("Numerador  : "))
        den = int(input("Denominador: "))
        resultado = num / den
        print(f"Resultado: {resultado:.4f}")
        break
    except ValueError:
        print("Error ValueError: solo números enteros.")
    except ZeroDivisionError:
        print("Error ZeroDivisionError: denominador no puede ser cero.")
```

---

### BLOQUE 13 — Decoradores

---

#### Pregunta 1 — @iniciar

**Prompt de explicación usado:**
```
¿Qué es un decorador en Python y cómo funciona internamente?
Muéstrame cómo crear el decorador @iniciar que imprima
"Iniciando..." antes de ejecutar cualquier función.
```

**Prompt de proceso similar:**
```
Pídeme crear un decorador @finalizar que imprima
"Proceso terminado." después de ejecutar la función.
```

**Mi resolución del proceso similar:**
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

#### Pregunta 2 — @positivo

**Prompt de explicación usado:**
```
¿Cómo creo un decorador que valide que el argumento
sea positivo antes de ejecutar la función?
Muéstrame con cuadrado(n).
```

**Prompt de proceso similar:**
```
Pídeme crear un decorador @no_cero que evite que una función
reciba 0 como argumento, retornando None en ese caso.
```

**Mi resolución del proceso similar:**
```python
def no_cero(func):
    def wrapper(n):
        if n == 0:
            print("El argumento no puede ser cero.")
            return None
        return func(n)
    return wrapper

@no_cero
def inverso(n):
    return 1 / n

print(inverso(0))   # → El argumento no puede ser cero. → None
print(inverso(4))   # → 0.25
```

---

#### Pregunta 3 — @log

**Prompt de explicación usado:**
```
¿Cómo creo un decorador @log que registre el nombre de la función,
sus argumentos y el resultado que retorna?
Muéstrame con suma(a, b).
```

**Prompt de proceso similar:**
```
Pídeme crear un decorador @cronometrar que mida cuánto tarda
una función en ejecutarse usando el módulo time.
```

**Mi resolución del proceso similar:**
```python
import time

def cronometrar(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"[{func.__name__}] tardó {fin - inicio:.4f}s")
        return resultado
    return wrapper

@cronometrar
def operacion_lenta():
    time.sleep(0.3)
    return "listo"

operacion_lenta()
# → [operacion_lenta] tardó 0.3001s
```

---

### BLOQUE 14 — Unpacking Avanzado

---

#### Pregunta 1 — *mitad

**Prompt de explicación usado:**
```
¿Cómo funciona el unpacking extendido en Python con *?
Muéstrame cómo desempaquetar (10,20,30,40) en primera, *mitad, ultima.
```

**Prompt de proceso similar:**
```
Pídeme desempaquetar una lista de 6 elementos: el primero,
los 4 del centro y el último en variables separadas.
```

**Mi resolución del proceso similar:**
```python
datos = [5, 10, 15, 20, 25, 30]
primero, *centro, ultimo = datos

print(primero)  # 5
print(centro)   # [10, 15, 20, 25]
print(ultimo)   # 30
```

---

#### Pregunta 3 — Merge de diccionarios con **

**Prompt de explicación usado:**
```
¿Cómo combino dos diccionarios en Python con **
sin modificar los originales?
```

**Prompt de proceso similar:**
```
Pídeme combinar un diccionario de datos personales y uno de datos académicos
en uno solo, y mostrar que los originales no cambiaron.
```

**Mi resolución del proceso similar:**
```python
personal   = {"nombre": "Angel", "edad": 18}
academico  = {"carrera": "Sistemas", "semestre": 3}

completo   = {**personal, **academico}

print(personal)   # {"nombre": "Angel", "edad": 18}  ← sin cambios
print(academico)  # {"carrera": "Sistemas", ...}      ← sin cambios
print(completo)   # todo combinado
```

---

### BLOQUE 15 — Programación Funcional

---

#### Pregunta 1 — map()

**Prompt de explicación usado:**
```
¿Para qué sirve map() en Python?
Muéstrame cómo aplicar una operación a todos los elementos
de una lista usando map() con lambda.
```

**Prompt de proceso similar:**
```
Pídeme usar map() para convertir una lista de Celsius a Fahrenheit:
[0, 20, 37, 100].
```

**Mi resolución del proceso similar:**
```python
celsius    = [0, 20, 37, 100]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
# → [32.0, 68.0, 98.6, 212.0]
```

---

#### Pregunta 2 — filter()

**Prompt de explicación usado:**
```
¿Cómo uso filter() con lambda para filtrar elementos
de una lista según una condición?
```

**Prompt de proceso similar:**
```
Pídeme usar filter() para obtener solo los nombres que
tengan más de 4 letras de una lista de nombres.
```

**Mi resolución del proceso similar:**
```python
nombres = ["Ana", "Carlos", "Luis", "Stephanie", "Eva"]
largos  = list(filter(lambda n: len(n) > 4, nombres))
# → ["Carlos", "Stephanie"]
```

---

#### Pregunta 3 — reduce()

**Prompt de explicación usado:**
```
¿Cómo funciona reduce() de functools en Python?
Muéstrame cómo multiplicar todos los elementos de una lista
paso a paso con reduce().
```

**Prompt de proceso similar:**
```
Pídeme usar reduce() para encontrar el máximo de una lista
sin usar max(). Que yo lo resuelva.
```

**Mi resolución del proceso similar:**
```python
from functools import reduce

numeros = [3, 7, 2, 9, 4]
maximo  = reduce(lambda a, b: a if a > b else b, numeros)
# → 9

# Proceso interno:
# reduce(f, [3,7,2,9,4])
# → f(3,7)=7 → f(7,2)=7 → f(7,9)=9 → f(9,4)=9
```

---

### BLOQUE 16 — Persistencia de Datos

---

#### Pregunta 1 — Archivos de texto

**Prompt de explicación usado:**
```
¿Cómo escribo y leo un archivo de texto en Python con open()?
¿Cuál es la diferencia entre modo "w" y "r"?
```

**Prompt de proceso similar:**
```
Pídeme hacer un programa que escriba 3 líneas en un archivo
y luego las lea e imprima numeradas.
```

**Mi resolución del proceso similar:**
```python
with open("datos.txt", "w") as f:
    f.write("POO\n")
    f.write("Python\n")
    f.write("Estructuras\n")

with open("datos.txt", "r") as f:
    lineas = f.readlines()

for i, linea in enumerate(lineas, 1):
    print(f"{i}. {linea.strip()}")
```

---

#### Pregunta 2 — JSON

**Prompt de explicación usado:**
```
¿Cómo guardo y cargo un diccionario en formato JSON en Python?
Muéstrame json.dump() y json.load() con un ejemplo.
```

**Prompt de proceso similar:**
```
Pídeme guardar una lista de 3 productos en JSON y luego cargarla,
mostrando solo los que cuestan más de $50.
```

**Mi resolución del proceso similar:**
```python
import json

productos = [
    {"nombre": "Laptop",  "precio": 900},
    {"nombre": "Mouse",   "precio": 25},
    {"nombre": "Monitor", "precio": 350},
]

with open("productos.json", "w") as f:
    json.dump(productos, f, indent=4)

with open("productos.json", "r") as f:
    data = json.load(f)

caros = [p for p in data if p["precio"] > 50]
for p in caros:
    print(f"{p['nombre']}: ${p['precio']}")
# → Laptop: $900
# → Monitor: $350
```

---

### BLOQUE 17 — Proyecto Integrador con Mixins

---

#### Pregunta 1 — PromedioMixin

**Prompt de explicación usado:**
```
¿Qué son los Mixins en Python?
¿Cómo integro PromedioMixin en una clase Estudiante
usando herencia múltiple?
```

**Prompt de proceso similar:**
```
Pídeme crear un SueldoMixin con calcular_bono(sueldo)
e integrarlo en una clase Empleado.
```

**Mi resolución del proceso similar:**
```python
class SueldoMixin:
    def calcular_bono(self, sueldo, porcentaje=0.10):
        return sueldo * porcentaje

class Empleado(SueldoMixin):
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

    def info(self):
        bono = self.calcular_bono(self.sueldo)
        print(f"{self.nombre} — Sueldo: ${self.sueldo} — Bono: ${bono:.2f}")

emp = Empleado("Angel", 800)
emp.info()  # → Angel — Sueldo: $800 — Bono: $80.00
```

---

#### Pregunta 2 — ValidacionUsuarioMixin

**Prompt de explicación usado:**
```
¿Cómo creo un Mixin que valide email y edad?
Muéstrame cómo integrarlo en una clase Usuario.
```

**Prompt de proceso similar:**
```
Pídeme crear un ConectividadMixin con validar_telefono()
e integrarlo en una clase Contacto.
```

**Mi resolución del proceso similar:**
```python
class ConectividadMixin:
    @staticmethod
    def validar_telefono(numero):
        return len(numero) == 10 and numero.isdigit()

class Contacto(ConectividadMixin):
    def __init__(self, nombre, telefono):
        self.nombre   = nombre
        self.telefono = telefono

    def registrar(self):
        if self.validar_telefono(self.telefono):
            print(f"{self.nombre} registrado con teléfono {self.telefono}")
        else:
            print("Teléfono inválido (debe tener 10 dígitos)")
```

---

#### Pregunta 3 — ExportarMixin

**Prompt de explicación usado:**
```
¿Cómo exporto datos a JSON y CSV usando un Mixin con herencia múltiple?
Muéstrame exportar_json() y exportar_csv() integrados en clase Reporte.
```

**Prompt de proceso similar:**
```
Pídeme crear un ExportarMixin que también exporte en formato XML simple.
```

**Mi resolución del proceso similar:**
```python
class ExportarMixin:
    def exportar_xml(self, datos, etiqueta="item"):
        xml = "<datos>\n"
        for item in datos:
            xml += f"  <{etiqueta}>\n"
            for clave, valor in item.items():
                xml += f"    <{clave}>{valor}</{clave}>\n"
            xml += f"  </{etiqueta}>\n"
        xml += "</datos>"
        return xml

class Reporte(ExportarMixin):
    def __init__(self, datos):
        self.datos = datos
    def mostrar(self):
        print(self.exportar_xml(self.datos, "producto"))
```

---

## 📊 Resumen General

| Nivel | Bloque | Prompts de explicación | Prompts de proceso similar | Total |
|-------|--------|----------------------|--------------------------|-------|
| Principiante | 0, 1, 2 | 8 | 8 | 16 |
| Intermedio | 3–11 | 18 | 18 | 36 |
| Avanzado | 12–17 | 12 | 12 | 24 |
| **TOTAL** | **18** | **38** | **38** | **76** |

---

<div align="center">

**IA:** Claude (Anthropic) — [claude.ai](https://claude.ai)
*Usada como herramienta de aprendizaje, no para copiar respuestas directas.*

</div>
