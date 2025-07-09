name = "hello world!" # Strings are Immutable

# name[0] = "R" # Not Possible

length = len(name) # Length of String 
print(length)

print("\nMethods...")
print(name.upper(), name) # UPPERCASE
print(name.lower()) # lowercase
print(name.capitalize()) # First character capital
print(name.title())

print("\nStrip...")
text = " hello world "
print(text.strip()) # Output : "hello world"
print(text.lstrip()) # Output : "hello world "
print(text.rstrip()) # Output : " hello world"

print("\nFinding and Replacing...")
text = "Python is fun and fun and fun"
print(text)
print(text.find("is")) # Output : 7 Index of first occurence
print(text.replace("fun", "awesome"))

print("\nSplit and Join...")
text = "Apples,Bananas,Pineapples"
print(text.split(","))

print("-".join(['Apples', 'Bananas', 'Pineapples']))

print("\nChecking String Properties...")
text = "Python123"
print(text.isalpha()) # Output : False
print(text.isdigit()) # Output : Flase
print(text.isalnum()) # Output : True
print(text.isspace()) # Output : False
