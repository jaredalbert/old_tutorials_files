oceans = ['Atlantic', 'Pacific', 'Indian', 'Arctic', 'noname']
oceans2 = sorted(oceans)
with open('oceans.txt', 'w') as f:
    for ocean in oceans2:
        f.write(ocean)
        f.write('\n')
f.close()



with open ('oceans.txt', 'r') as text:
    bio = text.read()
print(bio)

##
##
##
##
##
##
##try:
##    with open('sample_for_learning2.txt') as text:
##        bio = text.read()
##except FileNotFoundError:
##    bio = None
##print(bio)
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##f = open('C:/Users/jaredalbert/AppData/Local/Programs/Python/Python36-32/sample_for_learning.txt')
##text = f.read()
##f.close()
##print(text)
##x = []
####for char in text:
####    x.append(char)
##[x.append(y) for y in text]
##print(x)
