n = input('input n : ')
print(n)
print(type(n))

# fibonacci 수열 : 0 1 1 2 3 5 8 13 21 34 55 89
m = input('input m : ')
a, b = 0, 1
i = 0
while i < int(m):
    print(a, end=' ')
    a, b = b, a+b
    i += 1
print()
