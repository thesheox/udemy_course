


import pandas

data=pandas.read_csv("data.csv")
# data_dict=data.to_dict()
#colors=data_dict["Primary Fur Color"]
# gray=0
# red=0
# black=0
# print(colors)
# for color in colors:
#     if colors[color]=="Gray":
#         gray+=1
#     elif colors[color]=="Cinnamon":
#         red+=1
#     elif colors[color]=="Black":
#         black+=1
# print(gray)
# print(red)
# print(black)



grey_count=len(data[data["Primary Fur Color"]=="Gray"])
red_count=len(data[data["Primary Fur Color"]=="Cinnamon"])
black_count=len(data[data["Primary Fur Color"]=="Black"])
21

data_dict={
    "Fur Color":["Gray","Cinnamon","Black"],
    "count":[grey_count,red_count,black_count]

}
my_data_frame=pandas.DataFrame(data_dict)
print(my_data_frame)