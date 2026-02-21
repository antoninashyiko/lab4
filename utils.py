def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
def nsd(a, b):
    if b>a:
        a, b = b, a
    while b>0:
        a, b = b, a%b
    return a
