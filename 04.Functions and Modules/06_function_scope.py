def sum(a, b):
    # a and b are local variables
    c = a + b
    z = 1 # creates a local variable called z which is destroyed after this function returns
    print(z)
    return c

def any():
    z = 32 # Local Variable
    print("Hello")

any()

z = 8 # z is a global variable
print(sum(4, 6))
print(z)
