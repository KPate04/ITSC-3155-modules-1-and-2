#Khushi Patel
#Shiksha Kabra
#Eva Gunn
#Tyler Hudson

intList = []
for i in range(10):
    intList.append(int(input("Enter number " + str(i + 1) + ": ")))

appearOnceList = []
for value in intList:
    frequency = 0;
    for compVal in intList:
        if value == compVal:
            frequency = frequency + 1
    if (frequency == 1):
        appearOnceList.append(value)
        
print("Original List: " + str(intList))
print("Numbers that appeared once: " + str(appearOnceList))