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