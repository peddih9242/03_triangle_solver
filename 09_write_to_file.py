import pandas

trig_pythag = ["Pythagoras", "Trigonometry"]
length_1 = [4, 5]
length_2 = [3, 20.05]
given_angles = ["N/A", 76]
which_trig = ["N/A", "tan"]
answer = [5, 20.05]

results_dict = {
    "Calculation Type": trig_pythag,
    "Length 1": length_1,
    "Length 2": length_2,
    "Angle": given_angles,
    "Trig Type": which_trig,
    "Answer": answer
}

# create dataframe to write to file
results_frame = pandas.DataFrame(results_dict)
results_frame = results_frame.set_index("Calculation Type")

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