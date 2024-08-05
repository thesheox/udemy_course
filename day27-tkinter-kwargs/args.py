def add(*args):
    sum=0
    for n in args:
        sum+=n
    return sum,args[0]


print(add(1,2,3,4,5,6))