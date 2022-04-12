import json
with open ('states.json') as f:
    data = json.load(f)

for state in data['states']:
    del(state['area_codes'])



with open('new_state_json','w')as f:
    json.dump(data, f, indent = 2)


# print(state['name'], state['abbreviation'])


