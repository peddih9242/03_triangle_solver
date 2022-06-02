# import modules

import math
import pandas

# functions

# string checker, checks for valid input from mini lists
def string_checker(response, valid_list, error):

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
        return "invalid"


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


# formats trailing 0s off floats
def trail_formatting(var_number):
    var_number = round(var_number, 2)
    return "%g"%(var_number)

# gets answer for trigonometry
def trig_answer():
    # use questions to set up future questions
    angle_length = string_checker("Are you trying to find an angle or length? ", side_angle, "Please enter a valid option ('length' or 'angle').")

    soh_cah_toa = string_checker("Are you using sin, cos or tan? ", trig_valid, "Please enter sin, cos or tan.")
    which_trig.append(soh_cah_toa)

    if angle_length == "angle":

        given_angles.append("N/A")

        # get what is needed to calculate the angle, calculate and then print to user
        if soh_cah_toa == "sin":
            side_2 = num_check("Length of the hypotenuse: ", "Please enter a number above 0.")
            side_1 = num_check("Length of the opposite side: ", "Please enter a number above 0 and below the hypotenuse length.", side_2)
            desired_result = math.asin(side_1 / side_2)
        
        elif soh_cah_toa == "cos":
            side_2 = num_check("Length of the hypotenuse: ", "Please enter a number above 0.")
            side_1 = num_check("Length of the adjacent side: ", "Please enter a number above 0 and below the hypotenuse length.", side_2)
            desired_result = math.acos(side_1 / side_2)    
        
        else:
            side_1 = num_check("Length of the opposite side: ", "Please enter a number above 0.")
            side_2 = num_check("Length of the adjacent side: ", "Please enter a number above 0.")
            desired_result = math.atan(side_1 / side_2)    

        # set up numbers to be printed and append to list
        desired_result = math.degrees(desired_result)
        desired_result = trail_formatting(desired_result)
        desired_result = unit_format(desired_result, "°")
        side_1 = trail_formatting(side_1)
        side_2 = trail_formatting(side_2)
        
        length_1.append(side_1)
        length_2.append(side_2)
        answer.append(desired_result)
        return desired_result

    invalid_side = False
    trig_loop = True
    desired_result = 0

    while trig_loop:
        if angle_length == "length":
            length_2.append("N/A")
            # get what is needed to calculate the length
            which_side = string_checker("Do you have the hypotenuse, opposite or adjacent? ", side_valid, "Please enter a valid option.")

            if not invalid_side:
                side_1 = num_check("How long is your side? ", "Please enter a number above 0.")
                angle_size = num_check("How big is your angle? ", "Please enter a number above 0 and below 90.", 90)

            length_unit = string_checker("What unit is your length in? ", valid_units, "Please enter a valid unit!")

            # calculate length
            if soh_cah_toa == "sin":
                if which_side == "hypotenuse":
                    desired_result = side_1 * math.sin(math.radians(angle_size))

                elif which_side == "opposite":
                    desired_result = side_1 /  math.sin(math.radians(angle_size))

                else:
                    invalid_side = True

            elif soh_cah_toa == "cos":
                if which_side == "hypotenuse":
                    desired_result = side_1 * math.cos(math.radians(angle_size))

                elif which_side == "adjacent":
                    desired_result = side_1 / math.cos(math.radians(angle_size))
                
                else:
                    invalid_side = True

            else:
                if which_side == "adjacent":
                    desired_result = side_1 * math.tan(math.radians(angle_size))
                
                elif which_side == "opposite":
                    desired_result = side_1 / math.tan(math.radians(angle_size))
                
                else:
                    invalid_side = True

            # format answer if calculated and return
            if desired_result != 0:

                # set up numbers to be printed and append to list
                desired_result = trail_formatting(desired_result)
                angle_size = trail_formatting(angle_size)
                side_1 = trail_formatting(side_1)

                desired_result = unit_format(desired_result, length_unit)
                
                length_1.append(side_1)
                given_angles.append(angle_size)
                answer.append(desired_result)
                return desired_result

            if invalid_side:
                print("You need to enter a valid side!")
                continue

# gets answer for both trigonometry and pythagoras
def triangle_solver():
    
    # ask user a series of questions to figure out what calculation type
    # to use and calculate answer
    
    length_unit = string_checker("What units are your length(s) in? ", valid_units, "Please enter a valid unit!")
    two_side = string_checker("Do you have 2 sides? ", yes_no, "Please enter yes or no.")

    if two_side == "yes":
        
        third_side = string_checker("Do you need to find the third side? ", yes_no, "Please enter yes or no.")
        
        if third_side == "yes":

            getting_hyp = string_checker("Are you given the hypotenuse? ", yes_no, "Please enter yes or no.")
            
            if getting_hyp == "yes":

                # use pythagoras to calculate missing side                
                side_1 = num_check("Length of the hypotenuse: ", "Please enter a number above 0.")
                
                while True:
                    side_2 = num_check("Length of side 2: ", "Please enter a number above 0 and below {}.".format(side_1))
                    if side_2 < side_1:
                        break
                    print("Please make sure the hypotenuse is the longest side!")
                desired_result = ((side_1 ** 2) - (side_2 ** 2)) ** 0.5                

            else:
                side_1 = num_check("Length of side 1: ", "Please enter a number above 0.")
                side_2 = num_check("Length of side 2: ", "Please enter a number above 0.")
                desired_result = ((side_1 ** 2) + (side_2 ** 2)) ** 0.5
            
            # append stats to list for printing
            trig_pythag.append("Pythagoras")
            length_1.append(unit_format(side_1, length_unit))
            length_2.append(unit_format(side_2, length_unit))
            which_trig.append("None")            
            answer.append(unit_format, length_unit)

        else:
            
            # get what is needed to calculate angle and calculate
            what_have_1 = string_checker("Give me your first side: ", side_valid, "Please enter hypotenuse / opposite / adjacent.")

            have_check = True
            while have_check == True:
                what_have_2 = string_checker("Give me your second side: ", side_valid, "Please enter hypotenuse / opposite / adjacent.")
                have_list = [what_have_1, what_have_2]
            
                if what_have_2 == what_have_1:
                    print("Please enter a different side! (hypotenuse / opposite / adjacent)")
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
            
                                elif "adjacent" in have_list and "hypotenuse" in have_list:
                                    desired_result = math.acos(side_2 / side_1)
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
                        
                        else:
                            break

                    if "opposite" in have_list and "adjacent" in have_list:
                        which_trig.append("tan")
                        desired_result = math.atan(side_1 / side_2)
                    
                    # append stats to list for printing
                    trig_pythag.append("Trigonometry")
                    desired_result = math.degrees(desired_result)
                    answer.append(unit_format(desired_result, "°"))
                    length_1.append(unit_format(side_1, length_unit))
                    length_2.append(unit_format(side_2, length_unit))
                
                break
          

    else:
        
        
        
        what_side = string_checker("What side are you trying to get? ", side_valid, "Please enter a valid side!")
        
        # make sure they're not getting the side they have
        side_invalid = "invalid"
        while side_invalid == "invalid":     
            what_have_1 = string_checker("What side do you have? ", side_valid, "Please enter a valid side.")
            if what_have_1 != what_side:
                break

            print("Please don't enter the same sides!")

        side_1 = num_check("How long is your side? ", "Please enter a number above 0.")
        angle_size = num_check("What's the size of your angle? ", "Please enter a number above 0 and below 90.", 90)
        
        length_1.append(unit_format(side_1, length_unit))
        length_2.append(unit_format(angle_size, "°"))

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
            
            elif what_have_1 == "opposite":
                desired_result = side_1 / math.tan(math.radians(angle_size))
        
        # append stats to lists for printing
        trig_pythag.append("Trigonometry")
        answer.append(unit_format(desired_result, length_unit))

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

# gets answer for pythagoras
def pythagoras_ans():

    given_angles.append("N/A")
    which_trig.append("N/A")
    # ask if the user is trying to find the hypotenuse or not and get unit
    get_hypotenuse = string_checker("Are you trying to find the hypotenuse? ", yes_no, "Please enter yes or no.")
    length_unit = string_checker("What unit is your length in? ", valid_units, "Please enter a valid unit!")

    # take in length of given sides and calculate length of desired side

    if get_hypotenuse == "yes":

        side_1 = num_check("What is the length of side 1? ", "Please enter a number above 0.")   
        side_2 = num_check("What is the length of side 2? ", "Please enter a number above 0.")
        
        desired_side = ((side_1 ** 2) + (side_2 ** 2)) ** 0.5

    elif get_hypotenuse == "no":

        side_1 = num_check("What is the length of the hypotenuse? ", "Please enter a number above 0.")    
        side_2 = num_check("What is the length of the other side? ", "Please enter a number above 0 and below the hypotenuse length.", side_1)
        
        desired_side = ((side_1 ** 2) - (side_2 ** 2)) ** 0.5

    # set up numbers to be printed and append to list
    side_1 = trail_formatting(side_1)
    side_2 = trail_formatting(side_2)
    desired_side = trail_formatting(desired_side)
    desired_side = unit_format(desired_side, length_unit)

    length_1.append(side_1)
    length_2.append(side_2)
    answer.append(desired_side)
    return desired_side

# returns given item with units
def unit_format(format_num, unit):
    return "{} {}".format(format_num, unit)


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
    ["megametre", "megameter", "megametres", "megameters"],
    ["yds", "yards", "yd", "yard"],
    ["ft", "foot", "feet"]
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
    "Trig Type": which_trig,
    "Answer": answer
}

keep_going = "yes"
while keep_going == "yes":

    # ask questions and get triangle answer
    calc_answer = triangle_solver()

    print("Your answer is:", calc_answer)
    keep_going = string_checker("Do you want to do another calculation? ", yes_no, "Please enter yes or no.")

results_frame = pandas.DataFrame(results_dict, columns = ['Calculation Type', 'Length 1', 'Length 2', 'Angle', 'Trig Type', 'Answer'])
results_frame = results_frame.set_index('Calculation Type')
print(results_frame)

# note: remake your string checker, if they type "help" then print help (function parameter)