from sys import stdout

a, b, c = [int(_) for _ in input().split()]

print("First")
stdout.flush()

t = 10**10
print(t)
stdout.flush()

i = int(input())
assert 1 <= i <= 3
if i == 1:
    a += t
    big = a
elif i == 2:
    b += t
    big = b
else:
    c += t
    big = c

y = 3 * big - (a + b + c)
print(y)
i = int(input())
stdout.flush()
assert 1 <= i <= 3
if i == 1:
    a += y
elif i == 2:
    b += y
else:
    c += y

print((max(a, b, c) - min(a, b, c)) // 2)
