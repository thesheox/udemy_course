student_dict={
    "student":["John", "Smith", "Tom"],
    "score":[90,111,121]
}

# for (name, score) in sudent_dict.items():
#     print(name, score)

import pandas

student_df=pandas.DataFrame(student_dict)
# print(student_df)

#loop through

for (index,row) in student_df.iterrows():
    print(row.score)


