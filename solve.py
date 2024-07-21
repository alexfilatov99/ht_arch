def solve(a, b, c):
    if a == 0:
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

