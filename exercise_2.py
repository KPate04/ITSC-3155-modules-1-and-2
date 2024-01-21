#801353524

#initializes strings and takes user input
UserString = input("Enter your string: ")
strLowercase = ""
strUppercase = ""
#uses for & if loops to sort into uppercase/lowercase strings
for char in UserString:
    if char.islower():
        strLowercase += char
    elif char.isupper():
        strUppercase += char
#combines lowercase&uppercase strings and prints output
strOut = strLowercase + strUppercase
print(strOut)