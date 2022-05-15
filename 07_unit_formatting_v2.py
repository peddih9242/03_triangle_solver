# functions

# number checker, checks for float above 0 and below high if given
def num_check(question, error, high=None):
    
    have_high = False

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

# blank checking function, checks if a string input is blank
def not_blank(question, error):
    
    var_loop = True
    while var_loop:
        
    # take in response and check if it is blank
        response = input(question).lower()
        
        if response != "":
            return response
        else:
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

def trail_formatting(var_number):
    return "%g"%(var_number)

def unit_format(format_num, unit):
    return "{} {}".format(format_num, unit)

# main routine

# valid units for the user's answer

valid_units = [
    ["°", "degrees", "d"],
    ["cm", "centimetres", "centimetre", "centimeters", "centimeter"],
    ["km", "kilometres", "kilometre", "kilometers", "kilometer"],
    ["mm", "millimetres", "millimetre", "millimeters", "millimeter"],
    ["m", "metres", "metre", "meters", "meter"],
    ["mi", "miles", "mile"],
    ["in", "inches", "inch"],
    ["megametre", "megameter", "megametres", "megameters"]
    ["yards", "yds", "yd"]
]

for item in range(3):

    number = num_check("What number? ", "Please enter a number above 0")
    number = trail_formatting(number)

    unit = string_checker("What unit? ", valid_units, "Please enter a valid unit (for distance or angle size)")

    formatted = unit_format(number, unit)
    print(formatted)