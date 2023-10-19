# Reto No. 9.   “Así como digo una cosa, digo la otra”: Cantinflas.


Reto sobre Funciones Recursivas, Funciones sin nombre (anónima) lambdas, Argumentos por defecto y Argumentos no definidos (*args y **kwargs)


Desarrolle la mayoría de ejercicios en clase. Para cada punto cree un programa individual. Al finalizar suba todo a un repo.

1. De los retos anteriores seleccione 3 funciones y escribalas en forma de lambdas.

  a. Ejercicio 1: Cree una función que permita calcular el Máximo Comun Divisor de dos números dados (a y b).

  ```python
  if __name__ == '__main__': 
    # El usuario ingresa los números para calcular MCD
    numero1 = int(input("Ingrese el primer número entero: ")) 
    numero2 = int(input("Ingrese el segundo número entero: "))
    # La función lambda calcula el MCD
    respuesta = lambda a, b: a if b == 0 else respuesta(b, a % b) 
    # Si b = 0,  retorna a. Si b no es 0, se hace recursión a la misma función lambda
    # Se llama a la funcion tomando como argumnetos num1 y num 2
    mcd = respuesta(numero1, numero2)
    # Se imprime el resultado
    print("El máximo común divisor de " + str(numero1) + " y " + str(numero2) + " es: " + str(mcd))
  ```

  b. Ejercicio 2: Cree una función anónima que calcule:
  
  ![image](https://github.com/jeriosv/reto_9/assets/142249529/ffbeacda-77e4-467f-a4fd-d496be0ec089)
  
  ```python
  if __name__ == "__main__": 
  n = int(input("Ingrese valor de X: ")) # n se inicializa con el valor de x que ingresa el usuario
  # Funcion lambda para calcular f de X cuando x vale n
  suma = (lambda x : x / (x**(1/3)-1))(n) # Calcular la operación
  # Imprimir valor de f de X
  print("La función cuando X igual a " + str(n) + ", f de X es igual a " + str(suma)) 
  ```

  c. Ejercicio 3: Cree una función que reciba dos números y un parametro con el cual se decida si regresa el mayor o el menor, por defecto debe regresar el mayor.
  
  ```python
  # Definimos la función  
def mayor_menor(a,b, es_menor):
    if es_menor:
        return min(a,b) # Retorna el menor
    elif a == b:        # caso en el que son iguales
        print("Los números " + str(a) + " y " + str(b) + " son iguales.")
    else:
        return min(a,b) # Retorna el menor

if __name__ == "__main__": 
        # Ingresa el usuario los números
    a = float(input("Ingrese el número a: "))
    b = float(input("Ingrese el número b: "))
    
    # Llamar la función para obtener el mayor
    mayor = mayor_menor(a, b, es_menor=False)
    print("El número mayor es:" + str(mayor))
    
    # Llamar la función para obtener el menor
    menor = mayor_menor(a, b, es_menor=True)
    print("El número menor es:", menor)
  ```





2. De los retos anteriores seleccione 3 funciones y escribalas con argumentos no definidos (*args).


  ```python

  ```


3. Escriba una función recursiva para calcular la operación de la potencia.


  ```python

  ```


4. Utilice la siguiente plantilla de code para contar el tiempo:

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

  ```


5. Crear cuenta en stackoverflow y adjuntar imagen en el repo.
   

6. Cosas de adultos....ir a linkedin y crear perfil....NO IMPORTA que estén iniciando.
