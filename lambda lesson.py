def build_quadratic_function(a, b, c):
    #builds a quadratic function with constants a,b,c and input x
    return lambda x : a*x**2 + b*x + c

f= build_quadratic_function(2, 1, 3)
print(f(2))
    







'''#combine first and last names
name = lambda first, last: (first.strip().title() + ' ' + last.strip().title())

print (name(' me  ', '   YOU   '))

x = lambda : 'What? '
print(x())


sci_fi_writers = ['yack tucan', 'mary bloody', 'm. g. wells', 'Hi on Me']

sci_fi_writers.sort(key = lambda name: name.split(' ')[-1].lower())

for name in sci_fi_writers:
    print(name[0])
    #sci_fi_writers[name[0]].upper(), sci_fi_writers[name[1]].upper()
print(sci_fi_writers)'''
