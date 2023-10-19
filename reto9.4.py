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