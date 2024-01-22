#801353524

# function letters that counts letter duplication
def letters(string_input):
    count_letter = {}
    for char in string_input:
        #ensures counted chars are alphabetical
        if char.isalpha():
            lower_char = char.lower()
            count_letter[lower_char] = count_letter.get(lower_char, 0) + 1
    return count_letter
#user input
input_user = input("Enter a string: ")
#calls letters function and prints output with counted letters
dict_out = letters(input_user)
print(dict_out)

