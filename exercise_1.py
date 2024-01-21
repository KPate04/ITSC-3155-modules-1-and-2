#801353524

#initializes strings and takes user input
UserString = input("Enter your string: ")
RevString = ""
#reverses string through for loop
for char in reversed(UserString):
    RevString += char
#prints reversed string loop
print(RevString)