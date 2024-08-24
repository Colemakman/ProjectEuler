from functools import cache 


@cache
def fib(n):
    if n < 2:
        return 1
    return fib(n-1) + fib(n-2)


t, f, i = 0, 0, 0
while (f < 4000000):
    f = fib(i)
    if f % 2 == 0:
        t += f
    i += 1

print(t)
