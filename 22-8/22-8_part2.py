'''
Answer for the second section of the morning challenge for the 22-8 term 2
'''

#Iterates through a range from 2000 to 3200 using a for loop
for number in range(2000, 3201):
    #Divides the number by 7 and checks if the result is a whole number
    divided_7_num = float(number / 7)
    if divided_7_num.is_integer() is True:
        #Divides the number by 5 and checks if the result isn't a whole number
        divided_5_num = number / 5
        if divided_5_num.is_integer() is False:
            #Print the number if both conditions are meet
            print(number)