# def double(x):
#     return x * 2
#
# print(double(5))
#

double=lambda x:x*2
multiply=lambda x,y:x*y
add=lambda x,y,z:x+y+z
full_name=lambda first_name,last_name:first_name+" "+last_name

age_check=lambda age:True if age>=18 else False

print(age_check(12))

print("shayan","saeidian")
print(double(10))
print(multiply(2,4))
print(add(2,3,4))