### Error Types ###

'''Syntax Error'''
#print "Hola comunidad" # Error en la sintaxis

print ("Hola comunidad") #Forma correcta


'''Name Error'''
#print(variable) # Error ya que la variable no esta definida
variable_2 = 2
print(variable_2) #Forma correcta

'''Index Error'''
my_list = ["Python", "Swift", "Kotlin", "Dart", "Javascript"]
#print(my_list[7]) #Error el indice esta fuera del rango
print(my_list[1])
print(my_list[-5])

'''Module Not Found Error'''
#import maths #Error el nombre del modulo esta mal escrito o no existe
import math #Forma correcta

'''Atribute Error'''
#print(math.PI) #Error el nombre del atributo esta mal escrito o no existe
print(math.pi)

'''Key Error'''
my_dict = {"Nombre":"Francisco", "Apellido":"Lopez", "Edad":32}
#print(my_dict["Apelido"]) #Error el nombre de la key esta mal escrito o no existe
print(my_dict["Nombre"]) #Forma correcta

'''Type Error'''
#print(my_list["0"]) #El indice debe ser un integer no un string
print(my_list[0]) #Forma correcta

'''Import Error'''
#from math import PI #Error el nombre del atributo a importar esta mal escrito o no existe
from math import pi

'''Value Error'''
#my_int = int("10 Años") #Error no se puede transformar texto a integer
my_int = int("10") #Forma Correcta

'''Zero Division Error''' #Que sera 0_0
#print(4/0) #Error no se puede dividir entre 0
