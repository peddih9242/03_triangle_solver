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


# number checker, checks for float above 0 and prints both
# a number for calculating and a number for printing
def num_check(question, error):
    valid = False
    while not valid:
        try:
            # ask user for number
            response = float(input(question))
            if response <= 0:
                print(error)
            else:
                return ["%g"%(response), response]
        
        # if input is not a number print an error
        except ValueError:
            print(error)



# main routine