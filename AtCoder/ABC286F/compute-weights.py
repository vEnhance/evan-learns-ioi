mods = [4, 5, 7, 9, 11, 13, 17, 19, 23]
product = 1
for m in mods:
    product *= m

assert product == 1338557220

for m in mods:
    partial_product = product // m
    print(pow(partial_product, -1, m) * partial_product)
