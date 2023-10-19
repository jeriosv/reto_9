# Reto No. 9.   Recursividad. “Así como digo una cosa, digo la otra”: Cantinflas.


Reto sobre Funciones Recursivas, Funciones sin nombre (anónima) lambdas, Argumentos por defecto y Argumentos no definidos (*args y **kwargs)


Desarrolle la mayoría de ejercicios en clase. Para cada punto cree un programa individual. Al finalizar suba todo a un repo.

## 1. De los retos anteriores seleccione 3 funciones y escribalas en forma de lambdas.

  a. Ejercicio 1: Calcular la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.

  ```python
  if __name__ == '__main__':
    # Ingreso del usuario
    n_gallinas = int(input("Ingrese la cantidad de gallinas: "))
    m_gallos = int(input("Ingrese la cantidad de gallos: "))
    k_pollitos = int(input("Ingrese la cantidad de pollitos: "))
    cantidad_carne_aves = lambda n_gallinas, m_gallos, k_pollitos: (n_gallinas * 6) + (m_gallos * 7) + (k_pollitos * 1)
    # Calcular la cantidad de carne de aves
    cantidad_carne = cantidad_carne_aves(n_gallinas, m_gallos, k_pollitos)

    # Imprimir resultado
    print("La cantidad de carne de aves es:", cantidad_carne, "kilos.")
  ```

  b. Ejercicio 2: Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a 3300 cada una y H huevos a 350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.
  
  ```python
if __name__ == "__main__":
    # Ingreso del usuario
    panes = float(input("Ingrese la cantidad de panes: ")) 
    bolsas_leche = float(input("Ingrese la cantidad de bolsas de leche: "))
    huevos = float(input("Ingrese la cantidad de huevos: "))
    # Preguntar al usuario cual es el monto que va a pagar 
    saldo = float(input("Monto con el cual va a pagar: "))
    # Definir la funcion lambda para calcular 
    suma = lambda panes,bolsas_leche,huevos,saldo: (saldo-((panes*300)+(bolsas_leche*3300)+(huevos*350)))
    # Definir los argumentos que toma la funcion lambda
    vueltas = suma(panes,bolsas_leche,huevos,saldo)
# Imprimir el resultado
if vueltas < 0:
    print("Lo siento, falta por pagar: " + str(abs(vueltas)))
elif vueltas == 0:
    print("No hay vueltas.")
else:
    print("Sus vueltas son: " + str(vueltas))
  ```

  c. Ejercicio 3: Haga un programa que utilice una función para calcular el valor de un préstamo C usando interés compuesto del i por n meses.
  
  ```python
if __name__ == "__main__":
    # Ingreso del usuario
    prestamo_inicial = float(input("Ingrese Préstamo inicial: "))
    tasa_interes = float(input("Ingrese Tasa de interes: "))
    tiempo = float(input("Ingrese Tiempo en meses: "))
    # Se define la funcion lambda
    valor_final = lambda prestamo_inicial, tasa_interes, tiempo: prestamo_inicial * ((1 + tasa_interes / 100) ** tiempo)
    # Se llama a la funcion y se le pasan los argumentos
    valor_prestamo = valor_final(prestamo_inicial, tasa_interes, tiempo)
    # Imprimir el resultado
    print("El valor final del préstamo es: " + str(valor_prestamo))
  ```



## 2. De los retos anteriores seleccione 3 funciones y escribalas con argumentos no definidos (*args).

  a. Ejercicio 1. Haga un programa que utilice una función para calcular el valor de un préstamo C usando interés compuesto del i por n meses.
  
  ```python
# Función calcular_valor_prestamo con argumentos no definidos
def calcular_valor_prestamo(*args) -> float:
    prestamo = args[0]
    tasa_interes = args[1]
    meses = args[2]
    return prestamo * ((1 + tasa_interes / 100) ** meses)

if __name__ == '__main__':
    # Ingreso del usuario
    p = float(input("Ingrese préstamo inicial: "))
    t_i = float(input("Ingrese la tasa de interés: "))
    m = int(input("Ingrese Tiempo en meses: "))
    # Se llama a la funcion y toma los argumentos anteriormente dados por el usuario
    valor_prestamo = calcular_valor_prestamo(p, t_i, m)
    
    # Imprimir resultados
    print("El valor a pagar es de: " + str(valor_prestamo))
  ```

  b. Ejercicio 2. Una función matemática para calcular el volumen y el área superficial de una esfera y un cono. Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r1, r2 y h.
  
  ```python
import math

# Función calcular_volumen con argumentos no definidos
def calcular_volumen(*args):
    radio_esfera = args[0]
    radio_cono = args[1]
    altura_cono = args[2]

    volumen_esfera = (4/3) * (radio_esfera**3) * math.pi
    volumen_cono = (altura_cono/3) * (radio_cono**2) * math.pi
    return volumen_esfera + volumen_cono    

# Función calcular_area con argumentos no definidos
def calcular_area(*args):
    radio_esfera = args[0]
    radio_cono = args[1]
    altura_cono = args[2]
    area_esfera = 4 * math.pi * radio_esfera**2
    altura_oblicua = math.sqrt(altura_cono*2 + radio_cono*2)
    area_cono = (math.pi * radio_cono * altura_oblicua) + (math.pi * radio_cono**2)
    return area_esfera + area_cono

if __name__ == '__main__':
    # Ingreso del usuario
    rad_e = float(input("Ingrese el radio de la esfera en cm: "))
    rad_c = float(input("Ingrese el radio del cono en cm: "))
    alt_c = float(input("Ingrese la altura del cono en cm: "))
    # Se llama a las funciones y toman los argumentos anteriormente dados por el usuario
    vol = calcular_volumen(rad_e, rad_c, alt_c)
    area = calcular_area(rad_e, rad_c, alt_c)
    
    # Imprimir resultados
    print("El volumen de la figura es: " + str(vol) + " cm^3")
    print("El área de la figura es: " + str(area) + " cm^2") 
  ```

  c. Ejercicio 3. El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.
  
  ```python
# Función calcular_contagios con argumentos no definidos
def calcular_contagios(*args):
    contagios_actuales = args[0]
    dias_transcurridos = args[1]
    return contagios_actuales * (2 ** dias_transcurridos)

if __name__ == '__main__':
    # Ingreso del usuario
    c_a = int(input("Ingrese el número de contagiados actuales: "))
    d_t = int(input("Ingrese el número de días a partir de hoy: "))
    # Se llama a la funcion y toma los argumentos anteriormente dados por el usuario
    t_c = calcular_contagios(c_a, d_t)
    # Imprimir resultados
    print("El número total de personas contagiadas después de " + str(d_t) + " días es: " + str(t_c))
  ```


## 3. Escriba una función recursiva para calcular la operación de la potencia.


  ```python
# Funcion Potencia Recursivo con argumentos n y p siendo enteros
def PotenciaRecursivo(n : int,p : int)-> int:
  if p == 0: #si p es igual a 0 retorna 1
    return 1
  else: 
    # Sino Condicion de la funcion recursiva
    return n * PotenciaRecursivo(n,p-1) 


if __name__ == "__main__":
    # Ingreso del usuario 
    n = int(input("Ingrese un número entero: "))
    p = int(input("Potencia a calcular: "))
    # Se llama la funcion y que tome como argumentos n y p dados por e usuario previamente
    Potencia_de_n = PotenciaRecursivo(n,p) 
    # Imprimir resultado
    print(str(n) + " elevado a la " + str(p) + " es igual a "+ str( Potencia_de_n)) 
  ```


## 4. Utilice la siguiente plantilla de code para contar el tiempo:

  ```python
  import time

  start_time = time.time()
  # instrucciones sobre las cuales se quiere medir tiempo de ejecución
  end_time = time.time()
  
  timer = end_time - start_time
  print(timer)
  ```

Realice pruebas para calcular fibonacci con iteración o con recursión. Determine desde que número de la serie la diferencia de tiempo se vuelve significativa. 


  ```python
import time

# Función de recursión, su argumento n 
def fibonacci_recursion(n):
    if n <= 1: # si n es menor o igual a 1, retornar n
        return n 
    else:      # Sino se suman los dos números anteriores
        return fibonacci_recursion(n-1) + fibonacci_recursion(n-2) # 

# Funcion de iteración, su argumento n 
def fibonacci_iteracion(n):
    if n <= 1: # si n es menor o igual a 1, retornar n
        return n 
    else:      # sino retornar b ya que sera el el valor del Fibonacci actual porque a es el fibonacci anterior
        a, b = 0, 1 
        for i in range(n-1): # Para cada elemento (i) iterar n-1 veces 
            a, b = b, a + b # se suma el valor de a y b para crear un nuevo valor de b y a toma el valor anterior de b
        return b # 

n = int(input("Ingrese el valor de n: "))

# Medición del tiempo de Fibonacci con recursión
start_time_recursion = time.time()
fib_recursion = fibonacci_recursion(n)
end_time_recursion = time.time()
timer_recursion = end_time_recursion - start_time_recursion
print("El tiempo de ejecución de Fibonacci con recursión para n = " + str(n) + " fue de: " + str(timer_recursion) + " segundos.")

# Medicion del tiempo de Fibonacci con iteración
start_time_iteracion = time.time()
fib_iteracion = fibonacci_iteracion(n)
end_time_iteracion = time.time()
timer_iteracion = end_time_iteracion - start_time_iteracion
print("El tiempo de ejecución de Fibonacci con iteración para n = " + str(n) + " fue de: " + str(timer_iteracion) + " segundos.")
print("La diferencia de tiempo fue de " + str(abs(timer_recursion-timer_iteracion)) + " segundos que equivale al " +  str(100*abs(timer_recursion-timer_iteracion)/timer_recursion) + " por ciento.")

# Se compara los tiempos para imprimir una respuesta final
if timer_recursion > timer_iteracion:
    print("Fibonacci con iteración es más rápido que con recursión.")
else:
    print("Fibonacci con recursión es más rápido que con iteración.")
  ```


## 5. Crear cuenta en stackoverflow y adjuntar imagen en el repo.
   ![image](https://github.com/jeriosv/reto_9/assets/142249529/7b7728f8-b23f-4328-9aa4-b07b2653e6be)

   

## 6. Cosas de adultos....ir a linkedin y crear perfil....NO IMPORTA que estén iniciando.

![image](https://github.com/jeriosv/reto_9/assets/142249529/d63cc1a5-7804-4cdd-b5f3-48c32a0c5887)

www.linkedin.com/in/jaime-eduardo-ríos-villegas-049422297 

