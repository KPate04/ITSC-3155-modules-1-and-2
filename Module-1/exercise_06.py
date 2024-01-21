#Khushi Patel
#Shiksha Kabra
#Eva Gunn
#Tyler Hudson

rowVal = int(input("Enter a row number from 1 to 5: "))
columnVal = int(input("Enter a column number from 1 to 5: "))

rowCurrent = ""
for y in range(5):
    print(rowCurrent)
    rowCurrent = ""
    for x in range(5):
            if (x == columnVal - 1 and y == rowVal - 1):
                rowCurrent = rowCurrent + "1 "
            else:
                rowCurrent = rowCurrent + "0 "
print(rowCurrent)