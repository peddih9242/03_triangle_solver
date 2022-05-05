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
                return [response, "%g"%(response)]
        
        # if input is not a number print an error
        except ValueError:
            print(error)

def format_numbers(number):
    return "%g"%(number)
# main routine
for item in range(3):
    # get desired number
    take_numbers = num_check("What number? ", "Please enter a number above 0")
    
    # separate the returned list into a number that can be used
    # for printing, and the other for calculating
    calc_number = take_numbers[0]
    show_number = take_numbers[1]

    # print results
    print("You said {}".format(show_number))
    print()