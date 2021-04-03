# 1) Write a normal function that accepts another function as an argument. Output the result of that other function in your “normal” function.
def normal_1(fn, arg):
    print(fn(arg))

# 2) Call your “normal” function by passing a lambda function – which performs any operation of your choice – as an argument.
normal_1(lambda x: x * 3, 2)

# 3) Tweak your normal function by allowing an infinite amount of arguments on which your lambda function will be executed. 
def normal_2(fn, *args):
    for arg in args:
        print(fn(arg))

normal_2(lambda x: x * 3, 1, 2, 3, 4)

# 4) Format the output of your “normal” function such that numbers look nice and are centered in a 20 character column.
def normal_3(fn, *args):
    for arg in args:
        print(f'Output: {fn(arg) : ^20}')

normal_3(lambda x: x * 3, 1, 2, 3, 4)