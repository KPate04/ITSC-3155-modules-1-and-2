#Khushi Patel
#Shiksha Kabra
#Eva Gunn
#Tyler Hudson

def letterGrade(grade):
    if (grade >= 90):
        return "A"
    if (grade >= 80):
        return "B"
    if (grade >= 70):
        return "C"
    if (grade >= 60):
        return "D"
    return "F"
    
grade = input("Enter a grade from 0 to 100: ")
print("Your letter grade is:", letterGrade(int(grade)))