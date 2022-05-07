import math

# functions

# number checker, checks for float above 0 and below high if given
def num_check(question, error, high=None):
    
    if high:
        have_high = True

    valid = False
    while not valid:
        try:
            # ask user for number
            response = float(input(question))
            
            # check that number is above 0 and lower than high if given
            if response <= 0:
                print(error)
                continue
            
            if have_high:
                if response >= high:
                    print(error)
                    continue
            
            return response
        
        # if input is not a number print an error
        except ValueError:
            print(error)


# string checker, checks for valid input from a given list
def string_checker(question, valid_list, error):
    # loop taking in input and string checking process
    valid = False
    while not valid:

        # take input
        response = input(question).lower()

        # compare response with items in list
        for item in valid_list:
            if response == item or response == item[0]:
                return item
        else:
            print(error)

# main routine

side_valid = ["hypotenuse", "adjacent", "opposite"]

side_length = 5

which_side = string_checker("Are which side are you trying to find? ", side_valid)

get_angle = num_check("Enter your angle: ", "Please enter an angle between 0 and 360.", 360)

