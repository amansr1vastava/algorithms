def gcd(x, y): 
    while(y): 
        x, y = y, x % y 
    return x   

def lcm(a, b):
    mul = a * b
    Gcd = gcd(a,b)
    return int(mul/Gcd)

if __name__ == '__main__':
    a = list(map(int, input().split()))
    print(lcm(a[0], a[1]))

