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