num = int(input("Introduce un num: "))
total = 1

for i in range(2, num + 1):
    total *= i

print(total)