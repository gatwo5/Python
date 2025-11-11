#En caso de que no sea un tipo valido saldra error

entero = int(input('Introduce un numero entero: '))
decimal = float(input('Introduce un numero decimal: '))
cadena = str(input('Introduce una cadena de texto: '))

#Mostrar valor y tipo
print(entero,type(entero))
print(decimal,type(decimal))
print(cadena,type(cadena))

#guardar en booleanos
esEntero = isinstance(entero,int)
esDecimal = isinstance(decimal,float)
esCadena = isinstance(cadena,str)

#Todas las comprobaciones son correctas
print(esEntero and esDecimal and esCadena)

#Suma
print(entero + decimal)