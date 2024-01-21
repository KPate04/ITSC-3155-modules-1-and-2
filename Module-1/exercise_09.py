#Khushi Patel
#Shiksha Kabra
#Eva Gunn
#Tyler Hudson

stringInput = []
for n in range(5):
    stringInput.append(input("Enter a word: "))

stringOutput = ""
for n in range(5):
    stringOutput = ' '.join(stringInput)

print("Words: " + str(stringInput))
print("One string: " + stringOutput)