#Khushi Patel
#Shiksha Kabra
#Eva Gunn
#Tyler Hudson


inputStr = input("Enter your string: ")
n = -1
p = 0
outputArr = [[]]

for char in inputStr:
    n = n + 1
    if (n == 3):
        n = 0
        p = p + 1
        outputArr.append([])
    outputArr[p].append("")
    outputArr[p][n] = char
print(outputArr)