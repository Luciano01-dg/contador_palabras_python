 # Paso 1: Solicitar al usuario que ingrese la edad del cliente

edad= int(input("Por favor, ingrese la edad del cliente:  "))

 # Paso 2: Verificar si la edad ingresada cumple con le requisito para ingresar a la discoteca

#permitido= True
#if edad>= 18:
   
#   permitido= True
#else:
#  permitido= False  
#------------------------------------------
# se puede usar un ternario para simplificar 
permitido=True if edad>=18 else False
# en una sola linea se puede achicar el codigo
#-----------------------------------------

 # Paso 3: Mostrar al usuario si su cliente puede o no ingresar a la discoteca

if permitido:
  print("puedes entrar a la discoteca")
else:
 print("Lo siento mucho, no puedes entrar a la discoteca siendo menor de edad")
