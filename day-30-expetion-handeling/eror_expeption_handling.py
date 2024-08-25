# fruits=["apple","banana"]
#
#
#
# try:
#   file=open("test3.txt")
#   print(fruits[1])
# except FileNotFoundError:
#  file=open("test3.txt","w")
#  file.write("new file created")
# except IndexError as error_message:
#    print(error_message)
# else:
#     print("there is no eror")
#     content=file.read()
#     print(content)
# finally:
#     raise TypeError("i made this eror for test")



height=float(input("Enter your height in meter\n"))
weight=float(input("Enter your weight in kg\n"))

if height>3:
    raise ValueError("Height is greater than 3 meters")

bmi=weight/height**2
print(f"your bmi is:{bmi}")