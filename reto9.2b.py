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