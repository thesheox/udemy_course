students=[("shayan","A",60),("reyhane","B",76),("maziar","C",46)]

grade=lambda grades:(grades[0],grades[2]+100)

print(list(map(grade,students)))


pass_grade=lambda grades:(grades[2]>60)

print(list(filter(pass_grade,students)))

import functools
letters=["s","h","a","y","a","n"]
word=functools.reduce(lambda  x,y,:x+y,letters)
print(word)


usernames=["shayan","reyhane","maziar"]
passwords=["123123","5675756","353536"]

users=dict(zip(usernames,passwords))

for key,value in users.items():
    print(key,value)