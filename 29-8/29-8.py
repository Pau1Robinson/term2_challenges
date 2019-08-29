'''
Converts a string of hex values separated by spaces into ascii
'''

def convert_hex_num(num):
    '''
    Convert an individual hex value in decimal
    '''
    if num.isdigit() == False:
        if ord(num) > 70:
            #Takes the ascii value of a-f from hex and changes it to 10-15
            num = ord(num) - 87
        else:
            #Takes the ascii value of A-F from hex and changes it to 10-15
            num = ord(num) - 55
    return num

def main():
    '''
    Handles the main logic for converting hex to ascii
    '''
    #Output string
    output_string = ''

    #Asks the user for the string of hex to be converted
    user_input = input('Enter a string of hex values with spaces between\n')

    #Makes a list of the indexes of the spaces
    indices = [value for value in range(len(user_input)) if user_input[value] == ' ']
    indices.append(len(user_input))
    print(indices)

    for value in indices:
        #Get the hex value from user_input
        hex_first = user_input[value - 2]
        hex_second = user_input[value - 1]

        #Convert hex values to numbers
        hex_first = convert_hex_num(hex_first)
        hex_second = convert_hex_num(hex_second)
        print(hex_first)
        print(hex_second)

        #Convert hex to decimal
        decimal_num = (int(hex_first) * 16) + int(hex_second)
        output_string = f'{output_string}{chr(int(decimal_num))}'

    #Print output
    print(output_string)

if __name__ == "__main__":
    main()