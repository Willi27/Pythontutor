n = int(input())
m = int(input())

if n > m:
    print(1)
elif m%n == 0:
    print(m//n)
elif m%n != 0:
    print((m//n) + 1)
