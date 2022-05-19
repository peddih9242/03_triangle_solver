import pandas

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
                var_valid = True
                break
            else:
                var_valid = False
        
        # if response is found to be valid, return first item in valid list otherwise print error
        if var_valid == True:
            return response
        else:
            print(error)

def unit_format(format_num, unit):
    return "{} {}".format(format_num, unit)

# main routine

trig_pythag = ["Pythagoras", "Trigonometry"]
length_1 = [3, 6]
length_2 = [4, "N/A"]
angle = ["N/A", 53]
which_trig = ["N/A", "cos"]
answer = [5, 3.61]


results_dict = {
    "Calculation Type": trig_pythag,
    "Length 1": length_1,
    "Length 2": length_2,
    "Angle": angle,
    "Trig Type": which_trig,
    "Answer": answer
}

results_frame = pandas.DataFrame(results_dict, columns = ['Calculation Type', 'Length 1', 'Length 2', 'Angle', 'Trig Type', 'Answer'])
results_frame = results_frame.set_index('Calculation Type')
print(results_frame)
