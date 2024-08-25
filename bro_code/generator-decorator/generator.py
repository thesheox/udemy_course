# def create_cubes(n):
#     for x in range(n):
#         yield x**3
#
#
# for x in create_cubes(8):
#     print(x)
#
#
# def gen_fib(n):
#     a=1
#     b=1
#     for i in range(n):
#         yield a
#         a,b=(b,a+b)
#
#
# for x in gen_fib(10):
#     print(x)
#

def simple_gen():
    for x in range(3):
        yield x

# for x in simple_gen():
#     print(x)


y=simple_gen()
print(next(y))

s='hello'
s_itter=iter(s)

print(next(s_itter))