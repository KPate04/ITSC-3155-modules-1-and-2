#Khushi Patel
#Shiksha Kabra
#Eva Gunn
#Tyler Hudson

list1 = []
for i in range(5):
    newValue = int(input("Enter a number for the first list: "))
    list1.append(newValue)
    
list2 = []
for i in range(5):
    newValue = int(input("Enter a number for the second list: "))
    list2.append(newValue)

print("List 1: " + str(list1))
print("List 2: " + str(list2))

commonList = []
for val1 in list1:
    for val2 in list2:
        if val1 == val2:
            commonList.append(val1)
            
print("Common List: " + str(commonList))