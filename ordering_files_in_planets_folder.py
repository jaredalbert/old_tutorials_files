import os

os.chdir('C:/Users/jaredalbert/AppData/Local/Programs/Python/Python36-32/planets')

list_of_files = []

for file in os.listdir():
    file_name, file_ext = (os.path.splitext(file))

    print(file_name)

    f_planet, f_num = file_name.split('-')
    print(f_num)

    f_num = f_num.strip()[1:].zfill(2)
    f_planet = f_planet.strip()
    file_ext = file_ext.strip()

    #print('{}-{}-{}'.format(f_num, f_planet, file_ext))

    new_name ='{}-{}-{}'.format(f_num, f_planet, file_ext)

    os.rename(file, new_name)
       
 









##
##
##import os
##
##os.chdir('C:/Users/jaredalbert/AppData/Local/Programs/Python/Python36-32/planets')
##
##list_of_files = []
##
##for file in os.listdir():
##    file_name, file_ext = (os.path.splitext(file))
##    print(file_name, '   ', file_ext)
##    list_of_files.append(file_name)
##    
##precedence = lambda x: x[-1]
##
##list_of_files.sort(key = precedence)
##print(list_of_files)   
