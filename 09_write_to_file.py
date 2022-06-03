import pandas

trig_pythag = ["Pythagoras"]
length_1 = [4]
length_2 = [3]
given_angles = ["N/A"]
which_trig = ["N/A"]
answer = [5]

results_dict = {
    "Calculation Type": trig_pythag,
    "Length 1": length_1,
    "Length 2": length_2,
    "Angle": given_angles,
    "Trig Type": which_trig,
    "Answer": answer
}

results_frame = pandas.DataFrame(results_dict)
results_frame = results_frame.set_index("Calculation Type")
print(results_frame)
file_name = "triangle_stats.txt"
text_file = open(file_name, "w+")
text_file.write("eee")
text_file.write(results_frame)
text_file.close()