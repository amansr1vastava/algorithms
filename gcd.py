def gcd(x, y): 
    while(y): 
        x, y = y, x % y 
    return x     

if __name__ == "__main__":
    a = list(map(int, input().split()))
    print(gcd(a[0],a[1]))
