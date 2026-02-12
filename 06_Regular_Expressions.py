### Regular Expressions ###

import re

# match

my_string = "Esta es la leccion numero 7: Leccion llamada Expresiones Regulares"
my_other_string = "Esta no es la leccion numero 6: Manejo de Ficheros"

match = (re.match("esta es la leccion", my_string, re.I))
print(match)
start, end = (match.span())
print(my_string[start:end])

match = (re.match("Esta no es la leccion", my_other_string, re.I))
if not(match == None):
    print(match)
    start, end = (match.span())
    print(my_other_string[start:end])

print(re.match("Esta es la leccion", my_other_string))
print(re.match("Expresiones Regulares", my_string))#Match empieza desde el principio

# search

search = re.search("leccion", my_string)

print(search)
start, end = (search.span())
print(my_string[start:end])

# findall

findall = re.findall("leccion", my_string)
print(findall)

# split

print(re.split(":", my_string))

# sub

print(re.sub("Expresiones Regulares", "RegEx", my_string))
print(re.sub("leccion|Leccion", "LECCION", my_string))
print(re.sub("[l|L]eccion", "LECCION", my_string))

# patterns

pattern = r'[lL]eccion'
print(re.findall(pattern, my_string))

pattern = r'[lL]eccion|Expresiones'
print(re.findall(pattern, my_string))

pattern = r'[0-9]'
print(re.search(pattern, my_string))

pattern = r'\d'
print(re.findall(pattern, my_string))

pattern = r'\D'
print(re.findall(pattern, my_string))

pattern = r'[a].'
print(re.findall(pattern, my_string))

pattern = r'[a].*'
print(re.findall(pattern, my_string))

# email validation regular expression (regex)
email = "moraloiacono@gmail.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))

email = "moraloiacono@mandingo.plato"

print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))
