print("Break")
for i in range(1, 21):
    print(i)
    if (i == 11):
        break # Cancel the execution of this loop at 11

print("Continue")
for i in range(1, 21):
    if(i == 10):
        continue # Continue the loop for the next iteration here itself
    print(i)

print("Pass")
for i in range(1, 21):
    if(i == 10):
        print(i)
        pass # do nothing
