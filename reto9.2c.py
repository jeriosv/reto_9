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