#801353524

#sorts inputted values into unique list
def get_unique_list(list_input):
    return list(set(list_input))

#takes user input and puts user input into list
user_input = input("Enter your values with a space in between: ")

#converts string of inputs into integer lists
my_list = [int(item) for item in user_input.split()]

#calls get_unique_list function with sorted values and prints
unique_list = get_unique_list(my_list)
print(unique_list)
