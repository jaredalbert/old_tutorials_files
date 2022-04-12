
def logger (msg):

    def log_message():
        print('Log:', msg)

    return log_message

log_hi = logger('Hi!')
log_hi()



















###first_class functions
##
##def square (x):
##    return x * x
##
##def my_map (func, arg_list):
##    result = []
##    for i in arg_list:
##        result.append(func(i))
##
##    return result
##
##squares = my_map(square, [1, 2, 3, 4, 5])
##
##print(squares)
##
##def cube(x):
##    return x * x * x
##
##cubes = my_map(cube, [1, 2, 3, 4, 5])
##print(cubes)
