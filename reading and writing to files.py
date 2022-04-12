#file objects


with open('test.txt','r') as rf:
    with open('test_copy.txt','w') as wf:
        for line in rf:
            wf.write(line)

with open('test_copy.txt','r') as rf2:
    rf2.contents = rf2.read(1999)
    print(rf2.contents, end ='!')


    
##    for line in f:
##        print(line)
##    size_to_read = 10
##
##
##    f_contents = f.read(size_to_read)
##    print(f_contents, end = ' ')
##
##    f.seek(0)
##    
##    f_contents = f.read(size_to_read)
##    print(f_contents, end = ' ')
##    

##    while len(f_contents) >0 :
##        print(f_contents, end = ' *')
##        f_contents = f.read(size_to_read)
##

##f = open('test.txt','r')
##print(help(f))
##print(f.mode)
##f.close()
