#Khushi Patel
#Shiksha Kabra
#Eva Gunn
#Tyler Hudson

def matchSuffix(string1, string2):
    if (len(string1) > len(string2)):
        longStringLength = len(string1)
        shortStringLength = len(string2)
        if (string1[-1 * shortStringLength:] == string2):
            return True
        return False
    else:
        longStringLength = len(string2)
        shortStringLength = len(string1)
        if (string2[-1 * shortStringLength:] == string1):
            return True
        return False
        
string1 = input("Enter a string: ")
string2 = input("Enter another string: ")
    
print(matchSuffix(string1, string2))