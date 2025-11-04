cero = 0
uno = 1
resultado = 0

for i in range(1,10):
    print(resultado, end=" ")
    resultado = cero + uno
    cero = uno
    uno = resultado