
def func(n):
    if n == 1:
        return 0
    if n%2 == 0:
        return 1 + func(n/2)
    x = func(n+1);
    y = func(n-1);
    if x>y:
        return y+1
    else:
        return x+1

print func(7)
