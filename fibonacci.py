# Uses python3
def calc_fib(n):
    liste = []
    for i in range(n+1):
        if i<=1:
            liste.append(i)
        else:
            liste.append(liste[i-1]+ liste[i-2])
    return liste.pop()

n = int(input())
print(calc_fib(n))
