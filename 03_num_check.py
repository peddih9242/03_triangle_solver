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

# main routine
for item in range(3):
    number = num_check("What number? ", "Please enter a number above 0")
    print("You said {:.2f}".format(number))
    print()