

def gcd(higher: int, lower: int):
    if 0 == lower:
        return higher
    return gcd(lower, higher % lower)
