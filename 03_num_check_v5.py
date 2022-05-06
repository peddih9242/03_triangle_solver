# number checker, checks for float above 0 and below high if given
def num_check(question, error, high=None):
    
    if high:
        have_high = True

    valid = False
    while not valid:
        try:
            # ask user for number
            response = float(input(question))
            
            # check that number is above
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

def trail_formatting(var_number):
    return "%g"%(var_number)

# main routine
for item in range(2):

    # get angle size
    angle_check = num_check("Number between 0 and 360: ", "Please enter a number between 0 and 360 (1-359)", 360)
    no_zero = trail_formatting(angle_check)
    
    # show the inputted number and formatted number
    print("Inputted number: {}".format(angle_check))
    print("Formatted number: {}".format(no_zero))
    print()