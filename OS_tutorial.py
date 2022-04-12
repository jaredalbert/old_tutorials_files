import os
from datetime import datetime


#print(dir(os.getcwd))

#os.makedirs('testing_123.txt')


#os.removedirs('os_demo/sub_directory')
#mod_time= (os.stat( 'no_name_123').st_mtime)

#print(datetime.fromtimestamp(mod_time))


#print(os.listdir())
#for dirpath, dirname, filenames in os.walk('C:\\Users\\jaredalbert\\AppData\\Local\\Programs\\Python\\Python36-32'):
#   print(dirpath, dirname, filenames )

print(os.environ.get('HOME'))
##
##file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
##print(file_path)


##with_open(file_path, 'w') as f:
##    f.write()


print(dir(os.path))
