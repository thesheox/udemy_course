import random

list_of_people=[
    {
        "name":"kim kardashian",
        "followers":400,
        "country":"us",
        "job":"influencer",
        "choosed":False
    },
    {
        "name":"cristiano",
        "followers":600,
        "country":"portugal",
        "job":"football player",
        "choosed":False
    },
    {
        "name":"instagram",
        "followers":1000,
        "country":"uk",
        "job":"app",
        "choosed":False
    },
    {
        "name":"messi",
        "followers":300,
        "country":"arzhantin",
        "job":"footbal player",
        "choosed":False
    },

]
first_choice=random.choice(list_of_people)
second_choice=random.choice(list_of_people)
while first_choice["name"]==second_choice["name"]:
    first_choice = random.choice(list_of_people)
    second_choice = random.choice(list_of_people)
current_score=0
false_answer=False
while false_answer==False:
    print(first_choice["name"])
    print(second_choice["name"])
    higher_or_lower=input("who has more follower : A or B\n")
    if (higher_or_lower=="a" and first_choice["followers"]>second_choice["followers"]):
        current_score+=1
        print("you are right")
        for items in list_of_people:
            if items==second_choice:
                items["choosed"]=True
        second_choice = random.choice(list_of_people)
        while second_choice["choosed"]==True or first_choice["name"]==second_choice["name"]:
            second_choice = random.choice(list_of_people)

    elif (higher_or_lower=="b" and first_choice["followers"]<second_choice["followers"]):
        current_score += 1
        print("you are right")
        for items in list_of_people:
            if items == first_choice:
                items["choosed"] = True
        first_choice = random.choice(list_of_people)
        while first_choice["choosed"] == True or first_choice["name"]==second_choice["name"]:
            first_choice = random.choice(list_of_people)
    else:
        print("false answer")
        false_answer=True
