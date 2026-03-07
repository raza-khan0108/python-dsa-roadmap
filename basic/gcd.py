def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(10, 5))

def lcm(a,b):
    return int((a*b)/gcd(a,b))

print(lcm(10, 5))