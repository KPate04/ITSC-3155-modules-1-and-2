#Khushi Patel
#Shiksha Kabra
#Eva Gunn
#Tyler Hudson

i = int(input("Enter a number: "))

numList = []
sum = 0

for n in range(i):
    newFloat = float(input("Enter a number " + str(n+1) + ": "))
    sum = sum + newFloat
    numList.append(newFloat)

print("List: " + str(numList))

average = sum / i

print("Average: " + str(average))