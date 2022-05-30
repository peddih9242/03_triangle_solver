import math

# functions

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

def trig_answer():
    # use questions to set up future questions
    angle_length = string_checker("Are you trying to find an angle or length? ", side_angle, "Please enter a valid option ('side' or 'angle').")

    which_trig = string_checker("Are you using sin, cos or tan? ", trig_valid, "Please enter sin, cos or tan.")

    if angle_length == "angle":
        
        # get what is needed to calculate the angle, calculate and then print to user
        if which_trig == "sin":
            side_1 = num_check("Length of the opposite side: ", "Please enter a number above 0.")
            side_2 = num_check("Length of the hypotenuse: ", "Please enter a number above 0.")
            desired_result = math.asin(side_1 / side_2)
        
        elif which_trig == "cos":
            side_1 = num_check("Length of the adjacent side: ", "Please enter a number above 0.")
            side_2 = num_check("Length of the hypotenuse: ", "Please enter a number above 0.")
            desired_result = math.acos(side_1 / side_2)    
        
        else:
            side_1 = num_check("Length of the opposite side: ", "Please enter a number above 0.")
            side_2 = num_check("Length of the adjacent side: ", "Please enter a number above 0.")
            desired_result = math.atan(side_1 / side_2)    

        desired_result = math.degrees(desired_result)
        return desired_result

    invalid_side = False
    trig_loop = True
    desired_result = 0

    while trig_loop:
        if angle_length == "length":
            
            # get what is needed to calculate the length, calculate and then print to user
            which_side = string_checker("Do you have the hypotenuse, opposite or adjacent? ", side_valid, "Please enter a valid option.")

            if not invalid_side:
                side_1 = num_check("How long is your side? ", "Please enter a number above 0.")
                angle_size = num_check("How big is your angle? ", "Please enter a number above 0.", 90)

            if which_trig == "sin":
                if which_side == "hypotenuse":
                    desired_result = side_1 * math.sin(math.radians(angle_size))

                elif which_side == "opposite":
                    desired_result = side_1 /  math.sin(math.radians(angle_size))

                else:
                    invalid_side = True

            elif which_trig == "cos":
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

            if desired_result != 0:
                return desired_result

            if invalid_side:
                print("You need to enter a valid side!")
                continue


def new_trig():
    
    # ask user a series of questions to figure out what calculation type
    # to use and calculate answer
    
    two_side = string_checker("Do you have 2 sides? ", yes_no, "Please enter yes or no.")

    if two_side == "yes":
        
        third_side = string_checker("Do you need to find the third side? ", yes_no, "Please enter yes or no.")
        
        if third_side == "yes":

            getting_hyp = string_checker("Are you given the hypotenuse? ", yes_no, "Please enter yes or no.")
            
            if getting_hyp == "yes":
                # use pythagoras to calculate missing side
                side_1 = num_check("Length of side 1: ", "Please enter a number above 0.")
                side_2 = num_check("Length of side 2: ", "Please enter a number above 0.")
                desired_result = ((side_1 ** 2) + (side_2 ** 2)) ** 0.5

            else:
                side_1 = num_check("Length of the hypotenuse: ", "Please enter a number above 0.")
                side_2 = num_check("Length of side 2: ", "Please enter a number above 0 and below {}.".format(side_1))
                desired_result = ((side_1 ** 2) - (side_2 ** 2)) ** 0.5

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
                    side_1 = num_check("How long is your {}? ".format(what_have_1), "Please enter a number above 0.")
                    side_2 = num_check("How long is your {}? ".format(what_have_2), "Please enter a number above 0.")
            
                    if "hypotenuse" in have_list and "opposite" in have_list:
                        desired_result = math.asin(side_1 / side_2)
            
                    elif "adjacent" in have_list and "hypotenuse" in have_list:
                        desired_result = math.acos(side_1 / side_2)
            
                    elif "opposite" in have_list and "adjacent" in have_list:
                        desired_result = math.atan(side_1 / side_2)
            
                    else:
                        print("Something happened. That wasn't supposed to happen.")
                    
                break
            

    else:
        side_invalid = "invalid"
        while side_invalid == "invalid":
            what_side = string_checker("What side are you trying to get? ", side_valid, "Please enter a valid side!")
            what_have_1 = string_checker("What side do you have? ", side_valid, "Please enter a valid side.")
            if what_have_1 != what_side:
                break
            print("Please don't enter the same sides!")

        side_1 = num_check("How long is your side? ", "Please enter a number above 0.")
        angle_size = num_check("What's the size of your angle", "Please enter a number above 0 and below 90.", 90)
        
        if what_side == "hypotenuse":
        
            if what_have_1 == "opposite":
                desired_result = side_1 / math.sin(math.radians(angle_size))
        
            elif what_have_1 == "adjacent":
                desired_result = side_1 / math.cos(math.radians(angle_size))

        elif what_side == "opposite":

            if what_have_1 == "hypotenuse":
                desired_result = side_1 * math.sin(math.radians(angle_size))
            
            elif what_have_1 == "adjacent":
                desired_result = side_1 * math.tan(math.radians(angle_size))
        
        elif what_side == "adjacent":

            if what_have_1 == "hypotenuse":
                desired_result = side_1 * math.cos(math.radians(angle_size))
            
            elif what_have_1 == "opposite":
                desired_result = side_1 / math.tan(math.radians(angle_size))
    
    return desired_result

    
def trig_calc():
    have_valid = "invalid"
    while have_valid == "invalid":
        count = 0
        # ask user what they have, try and find
        what_have = input("What do you have? (e.g. opposite and angle): ")
        have_list = str.split(what_have)
        for item in have_list:

            if item == "opposite":
                opp = True

            elif item == "adjacent":
                adj = True

            elif item == "hypotenuse":
                hyp = True

            elif item == "angle":
                ang = True

            else:
                continue

            if ang == True or hyp == True or adj == True or opp == True:
                count += 1

            # once we have what we need to calculate exit loop
            if count == 2:
                break
            
        if count != 2:
            print("Please enter a valid option!")
            continue

# main routine

# string checking lists
side_angle = [
    ["length", "side length", "width"],
    ["angle", "angle size"]
    ]

trig_valid = [
    ["sin"],
    ["cos"],
    ["tan"]
]

side_valid = [
    ["hypotenuse", "hyp"],
    ["opposite", "opp"],
    ["adjacent", "adj"]
]

yes_no = [
    ["yes", "y"]
    ["no", "n"]
]

get_answer = trig_answer()

print("Your answer is: {:.2f}".format(get_answer))