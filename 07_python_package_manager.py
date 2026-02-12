### Python Package Manager ###

# pip https://pypi.org

import numpy

print(numpy.version.version)

np_array = numpy.array([1, 2, 3, 4, 5])

print(type(np_array))

print(np_array * 2)

import pandas
from package import aritmetics 
#pip list
#pip uninstall pandas
#pip show numpy
'''
import requests
import json

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response)
print(response.status_code)
print(response.json())
response_json = response.json()
pokemon_list = open("Python Intermedio\pokemon.json", "w+")
pokemon_json = json.dump(response_json, pokemon_list, indent = 8)
'''
# Arithmetics Package
import package

print(package.aritmetics.sum(1, 2))