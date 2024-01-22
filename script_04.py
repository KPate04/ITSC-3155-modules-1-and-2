#801353524

#ensures input is valid integer
def input_validity():
    while True:
        input_user = input("Enter an integer: ")
        try:
            user_number = int(input_user)
            return user_number
        #output in the case of incorrect input
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

#sum value
resulting_sum = 0
#calls input_validity for each input until 5 numbers has been reached
for num in range(5):
    num_user = input_validity()
    #adds new num to sum value
    resulting_sum += num_user
#prints resulting sum
print("Your sum is ",resulting_sum)
