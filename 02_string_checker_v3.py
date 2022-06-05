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

# main routine

yes_no = [
    ["yes", "sure", "okay"],
    ["no"]
    ]
    
for item in range(5):

    help_text = "In this question you are given two options, yes and no. You must pick either one to proceed through this program!"
    test_function = string_checker("Yes or no? ", yes_no, "Please enter yes or no", help_text)
    print("You said {}".format(test_function))
    print()