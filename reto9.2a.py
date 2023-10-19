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