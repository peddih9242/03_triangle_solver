from decimal import Decimal

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

# number checker, checks for float above 0
def num_check(question, error):
    valid = False
    while not valid:
        try:
            # ask user for number
            response = float(input(question))
            if response <= 0:
                print(error)
            else:
                return response
        
        # if input is not a number print an error
        except ValueError:
            print(error)

# formats trailing 0s off floats
def trail_formatting(var_number):
    return "%g"%(var_number)

# main routine

# set up valid string lists
yes_no = ["yes", "no"]

for item in range(2):
    # ask if the user is trying to find the hypotenuse or not
    get_hypotenuse = string_checker("Are you trying to find the hypotenuse?", yes_no, "Please enter yes or no.")

    # take in length of given sides and calculate length of desired side

    if get_hypotenuse == "yes":

        side_1 = num_check("What is the length of side 1? ", "Please enter a number above 0.")   
        side_2 = num_check("What is the length of side 2? ", "Please enter a number above 0.")
        
        desired_side = ((side_1 ** 2) + (side_2 ** 2)) ** 0.5

    if get_hypotenuse == "no":

        hypotenuse = num_check("What is the length of the hypotenuse? ", "Please enter a number above 0.")    
        side_1 = num_check("What is the length of the other side? ", "Please enter a number above 0.")
        
        desired_side = ((hypotenuse ** 2) - (side_1 ** 2)) ** 0.5

    # print missing side length
    desired_side = decimal.Decimal(desired_side)

    desired_side = trail_formatting(desired_side)


    print("The length of your missing side is: {}".format(desired_side))
    print()