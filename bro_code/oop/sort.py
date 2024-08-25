# students=["shayan","maziar","reyhane","ariyan"]
# students.sort(reverse=True)
# for i in students:
#     print(i)
#
#
# print(sorted(students))


students=[("shayan","A",60),("reyhane","B",76),("maziar","C",46)]

grade=lambda grades:grades[2]

print(sorted(students,key=grade))