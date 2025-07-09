# String Formatting

template = "Dear {}, you are awesome. Take this {}$ bag."

a1 = "John"
b1 = 10000

a2 = "Jack"
b2 = 1000

a3 = "Marie"
b3 = 300

s1 = template.format(a1, b1)
print(s1)

s2 = template.format(a2, b2)
print(s2)

s3 = template.format(a3, b3)
print(s3)

# f-strings
print(f"{a3} you are awesome take this {b1}$ bag.")
