x = ""

padding = "0" * 20

for i in range(1, 101):
    if i > 1:
        x += padding
    x += str(5**i)

print(x)
