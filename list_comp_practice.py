mega_list = [(10,{'first':1, 'second':'2'}),(20,{'first':'3', 'fourth':'4'})]
new_dict = [('a',{'first':'1'}),('b', {'second':2})]

noi = [n for n,d in mega_list if d['first']== '3']
#noi = [n for  n,d in mega_list if d[1] == '1']
#noi = [d for n,d  in new_dict if d[1]['first'] == 1]
#noi = [d['first'] for n,d  in new_dict] # if d[1]['first'] == 1]
print(noi)
#print(new_dict[1][1]['second'])
