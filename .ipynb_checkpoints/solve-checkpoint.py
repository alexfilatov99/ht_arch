import sys
def solve(a, b, c):
    a = float(a)
    b = float(b)
    c = float(c)
    if a < 1e-10:
        raise ValueError("Coefficient 'a' cannot be zero")
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return []
    elif discriminant == 0:
        x = -b / (2 * a)
        return [x, x]
    else:
        x1 = (-b + discriminant**0.5) / (2 * a)
        x2 = (-b - discriminant**0.5) / (2 * a)
        return [x1, x2]
if __name__ == "__main__":
    if len(sys.argv) != 4:
        raise ValueError("Invalid parameters")
    print(solve(sys.argv[1],sys.argv[2],sys.argv[3]))
