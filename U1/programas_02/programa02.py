"""
programa02
Escribe un programa que

 Cree una variable que almacene el número entero 6.

 Muestre por pantalla el tipo del objeto que contiene el número 6, y el tipo del objeto
al que apunta la variable (deben ser iguales)

 Cree otra variable a la que se asigne la primera variable.

 Muestre por pantalla el tipo del objeto que contiene el número 6 y el tipo del objeto
al que apunta la variable (deben ser iguales)

 Utilice los operadores de identidad (is e is not) para comprobar y mostrar por
pantalla que los dos variables apuntan al mismo objeto y por lo tanto a la misma
posición de memoria.

 Asigne la cadena “Hola” a la primera variable.

 Muestre por pantalla el tipo del objeto que contiene la cadena “Hola” y el tipo del
objeto al que apunta la variable (deben ser iguales) (y diferentes al objeto 6).

 Utilice la función isinstance() para comprobar y mostrar por pantalla que el
objeto al que apunta la primera variable es de tipo int y el de la segunda es de
tipo str.
"""

num = 6

print(id(6))
print(id(num))

num2 = num

print(id(6))
print(id(num2))

print(num is num2)
print(num is not num2)

num = "Hola"
print(id(num))
print(id("Hola"))

print(isinstance(num,str))
print(isinstance(num2,int))