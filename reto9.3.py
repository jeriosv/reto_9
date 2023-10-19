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