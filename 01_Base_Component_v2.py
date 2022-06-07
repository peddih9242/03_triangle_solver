# import modules

import math
import pandas

# functions

# string checker, checks for valid input from mini lists
def string_checker(question, valid_list, error, help_response):
    
    # loop taking in input and string checking process
    valid = False
    while not valid:
        
        # take input
        response = input(question).lower()
        
        # if the user asks for help then give help based on question
        if response == "help":
            print(help_response)

        else:
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
                print()


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
            print()


# formats trailing 0s off floats
def trail_formatting(var_number):
    var_number = round(var_number, 2)
    return "%g"%(var_number)


# gets answer for both trigonometry and pythagoras
def triangle_solver():
    
    # ask user a series of questions to figure out what calculation type
    # to use and calculate answer
    
    unit_help = "You should input the units that your lengths have (e.g. centimetres/cm), if you don't have units press <enter> to skip to the next question."
    length_unit = string_checker("What units are your length(s) in? ", valid_units, "Please enter a valid unit!", unit_help)
    two_side_help = "Do you have 2 sides that you know the length of?"
    two_side = string_checker("Do you have 2 sides? ", yes_no, "Please enter yes or no.", two_side_help)

    if two_side == "yes":
        
        third_side_help = "Do you need to find the side that you don't have?"
        third_side = string_checker("Do you need to find the third side? ", yes_no, "Please enter yes or no.", third_side_help)
        
        if third_side == "yes":

            hyp_help = "Are you given the longest side of your triangle?"
            given_hyp = string_checker("Are you given the hypotenuse? ", yes_no, "Please enter yes or no.", hyp_help)
            
            if given_hyp == "yes":

                # use pythagoras to calculate missing side                
                side_1 = num_check("Length of the hypotenuse: ", "Please enter a number above 0.")
                
                while True:
                    side_2 = num_check("Length of your other side: ", "Please enter a number above 0 and below {}.".format(side_1))
                    if side_2 < side_1:
                        break
                    print("Please make sure the hypotenuse is the longest side!")
                    print()
                desired_result = ((side_1 ** 2) - (side_2 ** 2)) ** 0.5                

            else:
                side_1 = num_check("Length of one side: ", "Please enter a number above 0.")
                side_2 = num_check("Length of the other side: ", "Please enter a number above 0.")
                desired_result = ((side_1 ** 2) + (side_2 ** 2)) ** 0.5
            
            # append stats to list for printing
            trig_pythag.append("Pythagoras")
            side_1 = trail_formatting(side_1)
            side_2 = trail_formatting(side_2)
            length_1.append(unit_format(side_1, length_unit))
            length_2.append(unit_format(side_2, length_unit))
            which_trig.append("N/A")    
            given_angles.append("N/A")     
            desired_result = trail_formatting(desired_result)
            desired_result = unit_format(desired_result, length_unit)
            answer.append(desired_result)

        else:
            
            # get what is needed to calculate angle and calculate
            what_have_help = "\nWe need to know if your side is the hypotenuse / opposite / adjacent. \n- If your side is the longest side, it's the hypotenuse. \n- If your angle is right next to the side you have, it's the adjacent. \n- If your side is on the other side of the angle, it's the opposite.\n"
            what_have_1 = string_checker("Give me one of the sides you have: ", side_valid, "Please enter a valid option (hypotenuse / opposite / adjacent)", what_have_help)

            have_check = True
            while have_check == True:
                what_have_2 = string_checker("Give me the other side you have: ", side_valid, "Please enter hypotenuse / opposite / adjacent.", what_have_help)
                have_list = [what_have_1, what_have_2]
            
                if what_have_2 == what_have_1:
                    print("Please enter a different side! (hypotenuse / opposite / adjacent)")
                    print()
                    continue
            
                else:
                    
                    while True:
                        side_1 = num_check("How long is your {}? ".format(what_have_1), "Please enter a number above 0.")
                        side_2 = num_check("How long is your {}? ".format(what_have_2), "Please enter a number above 0.")

                        # make sure if hyp given, hyp is longest side and calculate properly with hyp as longer side
                        
                        if what_have_1 == "hypotenuse":
                            if side_1 > side_2:
                                if "hypotenuse" in have_list and "opposite" in have_list:
                                    desired_result = math.asin(side_2 / side_1)
                                    which_trig.append("sin")
            
                                elif "adjacent" in have_list and "hypotenuse" in have_list:
                                    desired_result = math.acos(side_2 / side_1)
                                    which_trig.append("cos")
                                break
                            print("Please make sure the hypotenuse is the longest side!")
                        
                        elif what_have_2 == "hypotenuse":
                            if side_2 > side_1:
                                if "hypotenuse" in have_list and "opposite" in have_list:
                                    which_trig.append("sin")
                                    desired_result = math.asin(side_1 / side_2)
            
                                elif "adjacent" in have_list and "hypotenuse" in have_list:
                                    which_trig.append("cos")
                                    desired_result = math.acos(side_1 / side_2)
                                break
                            print("Please make sure the hypotenuse is the longest side!")
                            print()
                        
                        else:
                            break

                    if "opposite" in have_list and "adjacent" in have_list:
                        which_trig.append("tan")
                        if what_have_1 == "opposite":
                            desired_result = math.atan(side_1 / side_2)
                        elif what_have_2 == "opposite":
                            desired_result = math.atan(side_2 / side_1)
                    
                    # append stats to list for printing
                    trig_pythag.append("Trigonometry")
                    desired_result = math.degrees(desired_result)
                    desired_result = trail_formatting(desired_result)
                    desired_result = unit_format(desired_result, "°")
                    given_angles.append(desired_result)
                    answer.append(desired_result)
                    length_1.append(unit_format(side_1, length_unit))
                    length_2.append(unit_format(side_2, length_unit))
                
                break
          

    else:
        
        
        what_side_help = "\nWe need to know if the side is hypotenuse / opposite / adjacent. \n- If the side is the longest side, it's the hypotenuse. \n- If your angle is right next to the side you have, it's the adjacent. \n- If the side is on the other side of your angle, it's the opposite.\n"
        what_side = string_checker("What side are you trying to get? ", side_valid, "Please enter a valid option (hypotenuse / opposite / adjacent)", what_side_help)
        
        # make sure they're not getting the side they have
        side_invalid = "invalid"
        while side_invalid == "invalid":     

            what_have_1 = string_checker("What side do you have? ", side_valid, "Please enter a valid option (hypotenuse opposite / adjacent).", what_side_help)
            if what_have_1 != what_side:
                break

            print("Please don't enter the same sides!")
            print()

        side_1 = num_check("How long is the side you have? ", "Please enter a number above 0.")
        angle_size = num_check("What's the size of your angle? ", "Please enter a number above 0 and below 90.", 90)
        
        

        if what_side == "hypotenuse":
        
            if what_have_1 == "opposite":
                desired_result = side_1 / math.sin(math.radians(angle_size))
                which_trig.append("sin")

            elif what_have_1 == "adjacent":
                desired_result = side_1 / math.cos(math.radians(angle_size))
                which_trig.append("cos")

        elif what_side == "opposite":

            if what_have_1 == "hypotenuse":
                desired_result = side_1 * math.sin(math.radians(angle_size))
                which_trig.append("sin")

            elif what_have_1 == "adjacent":
                desired_result = side_1 * math.tan(math.radians(angle_size))
                which_trig.append("tan")
                
        elif what_side == "adjacent":

            if what_have_1 == "hypotenuse":
                desired_result = side_1 * math.cos(math.radians(angle_size))
                which_trig.append("cos")

            elif what_have_1 == "opposite":
                desired_result = side_1 / math.tan(math.radians(angle_size))
                which_trig.append("tan")

        # append stats to lists for printing
        trig_pythag.append("Trigonometry")
        side_1 = trail_formatting(side_1)
        angle_size = trail_formatting(angle_size)
        length_1.append(unit_format(side_1, length_unit))
        given_angles.append(unit_format(angle_size, "°"))
        desired_result = trail_formatting(desired_result)
        desired_result = unit_format(desired_result, length_unit)
        length_2.append(desired_result)        
        answer.append(desired_result)

    return desired_result

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

# returns given item with units
def unit_format(format_num, unit):
    return "{} {}".format(format_num, unit)

def instructions():
    instruction_help = "If you haven't used this program before, read the instructions."
    print_instructions = string_checker("Do you want to see the instructions? ", yes_no, "Please enter yes or no.", instruction_help)

    if print_instructions == "yes":
        print()
        print("**** Welcome to the Triangle Solver! ****")
        print("- In this program, you will be asked questions about your triangle.")
        print("- Answer those questions and this program will calculate the part of your triangle that you're looking for!")
        print("- It is important to note that if you don't understand a word question, you can type 'help' which will explain the question in a way that you can *hopefully* understand.")
        print("- You can do as many calculations as you want, and when you stop the stats for each calculation will be written to a .txt file under the name 'triangle_stats.txt'.")
    print()
    return ""


# main routine

# string checking lists

yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

side_angle = [
    ["length", "side length", "width", "side", "l"],
    ["angle", "angle size", "a"]
]

trig_valid = [
    ["sin", "s"],
    ["cos", "c"],
    ["tan", "t"]
]

side_valid = [
    ["hypotenuse", "hyp", "h"],
    ["opposite", "opp", "o"],
    ["adjacent", "adj", "a"]
]

valid_units = [
    ["cm", "centimetres", "centimetre", "centimeters", "centimeter"],
    ["km", "kilometres", "kilometre", "kilometers", "kilometer"],
    ["mm", "millimetres", "millimetre", "millimeters", "millimeter"],
    ["m", "metres", "metre", "meters", "meter"],
    ["mi", "miles", "mile"],
    ["in", "inches", "inch"],
    ["megametres", "megameter", "megametre", "megameters"],
    ["yds", "yards", "yd", "yard"],
    ["ft", "foot", "feet"],
    ["", "no unit", "none", "n"]
]

trig_pyth_valid = [
    ["trigonometry", "trig", "t"],
    ["pythagoras", "pythagoras theorem", "pythag", "p"]
]

trig_pythag = []
length_1 = []
length_2 = []
given_angles = []
which_trig = []
answer = []

# set up dictionary for results
results_dict = {
    "Calculation Type": trig_pythag,
    "Length 1": length_1,
    "Length 2": length_2,
    "Angle": given_angles,
    "Function": which_trig,
    "Answer": answer
}

instructions()

keep_going = "yes"
while keep_going == "yes":
    
    print()
    # ask questions and get triangle answer
    calc_answer = triangle_solver()

    print()
    print("Your answer is:", calc_answer)
    keep_going_help = "If you want to keep going, enter yes, otherwise enter no to exit."
    keep_going = string_checker("Do you want to do another calculation? ", yes_no, "Please enter yes or no.", keep_going_help)

print("\n\n")
print("**** Triangle Solver Stats ****")
print()
results_frame = pandas.DataFrame(results_dict, columns = ['Calculation Type', 'Length 1', 'Length 2', 'Angle', 'Function', 'Answer'])
results_frame = results_frame.set_index('Calculation Type')
print(results_frame)

# change dataframe to text for writing to file
results_txt = pandas.DataFrame.to_string(results_frame)

# set up write to file
file_name = "triangle_stats.txt"
text_file = open(file_name, "w+")

# heading
text_file.write("**** Triangle Solver Stats ****")
text_file.write("\n\n")
text_file.write(results_txt)
text_file.close()