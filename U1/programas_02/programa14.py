bytes_iniciales = int(input('Introduce los bytes: '))

resto = bytes_iniciales
gb_dec = resto // 1000000000
resto %= 1000000000
mb_dec = resto // 1000000
resto %= 1000000
kb_dec = resto // 1000
b_dec = resto % 1000

resto = bytes_iniciales
gb_bin = resto // (1024 ** 3)
resto %= 1024 ** 3
mb_bin = resto // (1024 ** 2)
resto %= 1024 ** 2
kb_bin = resto // 1024
b_bin = resto % 1024

print(f"{bytes_iniciales} bytes en sistema decimal (SI): {gb_dec} GB, {mb_dec} MB, {kb_dec} KB, {b_dec} bytes")
print(f"{bytes_iniciales} bytes en sistema binario (IEC): {gb_bin} GiB, {mb_bin} MiB, {kb_bin} KiB, {b_bin} bytes")