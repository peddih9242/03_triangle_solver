# import modules


# functions

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


# function to round numbers to 2dp
def round_2dp(want_round):
    return round(want_round, 2)

# main routine

