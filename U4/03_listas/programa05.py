lista_numeros = [5,1,10,12,7,2]

# --- ORDENAR ---

lista_numeros.sort()

print(lista_numeros)

# ---

lista_ordenada = sorted(lista_numeros) 

print(lista_ordenada)

# --- CONCATENAR ---

lista1 = ['hola', 'buenos', 'dias']
lista2 = [1,2,3]

lista_concatenada = lista1 + lista2
lista1.extend(lista2)

print(lista_concatenada)
print(lista1)

# --- DIFERENCIA DE COPIA---

lista_copia = lista1

print(id(lista_copia))
print(id(lista1))

