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


# string checker, checks for valid input from mini lists
def string_checker(question, valid_list, error):
    
    # loop taking in input and string checking process
    valid = False
    while not valid:
        
        # take input
        response = input(question).lower()

        # compare response with items in list
        for var_list in valid_list:
            if response in var_list:
                response = var_list[0]
                valid = True
                break
            else:
                valid = False
        
        # if response is found to be valid, return first item in valid list otherwise print error
        if valid == True:
            return response
        else:
            print(error)

# main routine

side_angle = [
    ["length", "side length", "width"],
    ["angle", "angle size"]
    ]

trig_valid = [
    ["sin"],
    ["cos"],
    ["tan"]
]

angle_length = string_checker("Are you trying to find a side or length? ", side_angle, "Please enter a valid option ('side' or 'angle').")

which_trig = string_checker("Are you using sin, cos or tan? ", trig_valid, "Please enter sin, cos or tan.")