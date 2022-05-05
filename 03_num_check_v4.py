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
                return response
        
        # if input is not a number print an error
        except ValueError:
            print(error)

def trail_formatting(var_number):
    return "%g"%(var_number)

# main routine
for item in range(3):
    # get desired number and format it so that it doesn't have trailing 0s
    take_numbers = num_check("What number? ", "Please enter a number above 0")
    no_zero = trail_formatting(take_numbers)

    # show the inputted number and formatted number
    print("Inputted number: {}".format(take_numbers))
    print("Formatted number: {}".format(no_zero))