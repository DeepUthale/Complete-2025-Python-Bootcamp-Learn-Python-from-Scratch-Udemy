age = int(input("What is your Age?\n"))

if(age > 18):
    print("You can Drive!")
    print("Thank you")
elif(age == 18 ):
    print("Let's Schedule an Interview.")
elif(age == 0):
    print("Atleast Walk First!")
else:
    print("Sorry you cannot Drive.")
print("End of program.")
