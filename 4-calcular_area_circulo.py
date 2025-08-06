import math

# Paso 1 Solicitar al usuario que ingre el radio del circulo.

radio = float(input("Por favor, ingrese el radio del circulo:  "))

# Paso 2: Calcular el area del circulo utilizando la formula area= Ò * radio^2

area = math.pi * (radio**2)   #** simbolo al cuadrado

# Paso 3: Mostrar al usuario el area calculada

print("El area del circulo con radio", radio, "es:", area)