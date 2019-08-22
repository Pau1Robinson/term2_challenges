'''
Answer for the third section of the morning challenge for the 22-8 term 2
'''

#Asks the user for a string of two digit numbers separated by comma's
user_input = input('input a string of two digit numbers separated by comma\'s\n')
#test_input = '34,67,55,33,12,98'

#Delares the new list and tuple
new_list = []
new_tuple = ()

#Makes a list of the indices of the comma's in user_input
indices = [value for value in range(len(user_input)) if user_input[value] == ',']
indices.append(len(user_input))

#Iterates through the values in indices extracts the numbers into new_list and new_tuple
for value in indices:
    num = (user_input[value - 2]) + (user_input[value - 1])
    new_list.append(num)
    new_tuple = new_tuple + (num,)
#Prints new_list and new_tuple
print(str(new_list) + str(new_tuple))