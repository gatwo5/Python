import json

cadena_json = '''
[
{"nombre": "Chile", "moneda": "Peso chileno"},
{"nombre": "Egipto", "moneda": "Libra egipcia"}
]
'''

data = json.loads(cadena_json)

print(type(data))

for d in data:
    print(f"La moneda de {d['nombre']} es {d['moneda']}")