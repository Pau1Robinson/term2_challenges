'''
Answer for the first section of the morning challenge for the 22-8 term 2
'''

#Asks the user for the numbers for the begining and end of the range
input_min = input('input the number for the begining of the range to be printed\n')
input_max = input('input the number for the end of the range to be printed\n')

#Iterates through the range using input_min and input_max in a for loop and prints the output
for number in range(int(input_min), (int(input_max) + 1)):
    print(number)