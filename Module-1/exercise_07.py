#Khushi Patel
#Shiksha Kabra
#Eva Gunn
#Tyler Hudson

list = []
userInput = input("Enter a number or QUIT to quit: ")
while (userInput != "QUIT"):
    list.append(int(userInput))
    userInput = input("Enter a number or QUIT to quit: ")

print("All nums: " + str(list))

evenNumbers = [];
for value in list:
    if (value % 2 == 0):
        evenNumbers.append(value)

print("Even numbers: " + str(evenNumbers))