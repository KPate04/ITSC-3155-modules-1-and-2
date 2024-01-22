#801353524

#get_combined_dict function
def get_combined_dict(dict_1, dict_2):

    dict_combined = {}
    common_keys = set(dict_1.keys()) & set(dict_2.keys())
    for key in common_keys:
        dict_combined[key]=dict_1[key]+dict_2[key]
    return dict_combined

#test code
my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
combined_dict = get_combined_dict(my_dict_1, my_dict_2)
print(combined_dict)

#   input for first and second dictionaries
#input_dict1 = input("Enter first dictionary in the format key1:num1 key2:num2 - ")
#my_dict_1 = dict(item.split(':') for item in input_dict1.split())
#input_dict2 = input("Enter second dictionary in the format key1:num1 key2:num2 - ")
#my_dict_2 = dict(item.split(':') for item in input_dict2.split())
#   formatting & converting values to integers 
#my_dict_1 = {key: int(value) for key, value in my_dict_1.items()}
#my_dict_2 = {key: int(value) for key, value in my_dict_2.items()}
#   calls function & combines dictionaries
#combined_dict = get_combined_dict(my_dict_1, my_dict_2)
#   print combined_dict
#print(combined_dict)
