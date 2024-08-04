import random
rand=random.randint(1,13)
rand_num=["one","two","three","four","five","six","seven","eight","nine","ten"]
rand_num[0]="number one"
rand_num.append("eleven")
rand_num.extend(["twelve","thirteen"])
print(random.choice(rand_num))