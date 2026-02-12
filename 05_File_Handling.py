### File Handling ###
import os

#.txt file

txt_file = open("Python Intermedio/my_file.txt", "w+") # r+ es para leer y escribir
txt_file.write("Nombre: Fernando\nApellido: Rodriguez\nEdad: 24\nLenguaje Preferido: Pyhton")
#print(txt_file.read())
#print(txt_file.read(10))
#print(txt_file.readline())
txt_file.close()
txt_file = open("Python Intermedio/my_file.txt", "r+")


for line in txt_file.readlines():
    print(line.replace(":", ""))

txt_file.write(", aunque tambien me gusta Kotlin")

print(txt_file.read())

txt_file.close()

#os.remove("Python Intermedio/my_file.txt")

# .json file

import json

json_file = open("Python Intermedio/my_file.json", "w+")

json_test = {
    "name": "Tomas",
    "surname":"Alvarez",
    "age": 20,
    "city": "Cuba",
    "languaje":["Swift", "Python", "Kotlin"],
    "website" : "https://github.com/TomasAlvarez45"}

json.dump(json_test, json_file, indent=2)

json_file.close()

with open("Python Intermedio/my_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)



json_dict = json.load(open("Python Intermedio/my_file.json"))

print(type(json_dict))
print(json_dict["name"])

# .csv file

import csv

csv_file = open("Python Intermedio/my_file.csv", "w+")

csv_writer = csv.writer(csv_file)

csv_writer.writerow(["name, surname, age, city, languajes, website"])
csv_writer.writerow(["Hector, Lopez, 20, Cancun, Python, https://github.com/TomasAlvarez45"])
csv_writer.writerow(["Brais, Moure, 35, Galicia, Python, https://github.com/MoureDev"])

csv_file.close()

with open("Python Intermedio/my_file.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line)



# .xlsx file

import xlrd

# .xml file

import xml