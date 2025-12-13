a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]
res = set(a) & set(b)
print(res)

res = set(a) - set(b)
print(res)

res = set(b) - set(a)
print(res)

res = set(b) | set(a)
print(res)