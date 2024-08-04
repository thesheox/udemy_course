import random
repeat="yes"
while(repeat!="no"):
    my_choice=int(input("what do you chose? type 0 for rock and 1 for paper and 2 for scissors"))
    comuter_choice=random.randint(0,2)
    print(comuter_choice)
    if(my_choice==comuter_choice):
        print("draw")
    if (my_choice > comuter_choice):
        print("win")
    if(my_choice < comuter_choice):
        print("lose")
    repeat=input("repeat?")