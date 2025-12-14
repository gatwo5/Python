tupla = (1,2,3)

num1, num2, num3 = tupla

print(num1,num2,num3)

tupla2 = (1,2,3,4,5,6)

inicio, *otros, final = tupla2

print(inicio, otros, final)

def media(*args):
    return sum(args) / len(args)

print(media(1,2,3))