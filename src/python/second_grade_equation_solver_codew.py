from math import sqrt

def sec_deg_solver (a,b,c):

    if a == 0:
        
        if b != 0 and c != 0:
            x = -c / b
            return f"It is a first degree equation. Solution: {x}"
        
        if b == 0 and c == 0:
            return "The equation is indeterminate"
        
        if b == 0 and c != 0:
            return "Impossible situation. Wrong entries"
        
        if c == 0 and b != 0:
            x = 0.0
            return f"It is a first degree equation. Solution: {x}"
        
    raiz = b**2-4*a*c

    if raiz > 0:
        x = (-b + sqrt(raiz)) / (2 * a)
        y = (-b - sqrt(raiz)) / (2 * a)
        x = round(x, 10)
        y = round(y, 10)
        if x > y:
            return f"Two solutions: {y}, {x}"
        if x < y:
            return f"Two solutions: {x}, {y}"

    if raiz < 0:
        return "There are no real solutions"
    
    if raiz == 0:
        x = -b / (2*a)
        return f"It has one double solution: {x}"
assert sec_deg_solver(10, 2, -4) == "Two solutions: -0.7403124237, 0.5403124237"