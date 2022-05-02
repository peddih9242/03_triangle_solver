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

# main routine

yes_no = ["yes", "no"]
for item in range(5):
    test_function = string_checker("Yes or no? ", yes_no, "Please enter yes or no")
    print("You said {}".format(test_function))
    print()