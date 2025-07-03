student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas as pd
# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     print(row)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

data = pd.read_csv("nato_phonetic_alphabet.csv")
for (index, row) in data.iterrows(): 
    pass

#TODO 1. Create a dictionary in this format:
nato_ab = {row.letter: row.code for (index, row) in data.iterrows()}
# print(nato_ab)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
to_code = list(input("Enter a word: ").upper())
output_list = [nato_ab[l] for l in to_code]
print(output_list)
