# import csv
#
# with open("weather_data.csv") as weather:
#     data = csv.reader(weather)
#     temperatures = []
#     for row in data:
#         if row[1]!="temp":
#             temperatures.append(row[1])
#         print(row)
#     print(temperatures)


import pandas

data=pandas.read_csv("weather_data.csv")
# data_dict=data.to_dict()
# print(data_dict)
# temp_list=data["temp"].to_list()
# print(temp_list)
# print(data["temp"].mean())
# print(data["temp"].max())
#
# print(data[data.temp==data.temp.max()])
# print(data)
# print(data["temp"])

# monday=data[data.day=="Monday"]
# print(monday.temp)

#create adata frame

data_dict={
    "students":["Amy","James","Angela"],
    "scores":[76,56,65]
}

my_data=pandas.DataFrame(data_dict)
my_data.to_csv("new_data.csv")
