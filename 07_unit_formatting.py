def unit_format(format_num, unit):
    return "{}{}".format(format_num, unit)

# main routine

num_test_data = [50, 4, 60, 4, 30]

unit_test_data = ["degrees", "cm", "metres", "km", "°"]

for item in num_test_data:
    for var_item in unit_test_data:
        formatted = unit_format(item, var_item)
        print(formatted)