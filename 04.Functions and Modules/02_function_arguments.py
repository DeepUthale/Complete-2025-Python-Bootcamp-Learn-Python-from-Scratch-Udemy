# Positional Arguments
def add(a, b, plus = 1): # Default Arguments
    x = a + b + plus
    return x

c = add(3, 5, 2)
print(c)

c1 = add(b = 5, a = 3) # Keyword Arguments
print(c1)
