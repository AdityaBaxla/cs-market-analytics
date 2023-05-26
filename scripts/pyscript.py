import json

file = open('../data/c9london.json','r')

data = json.load(file)
#print(data)
for i in data['prices']:
    print(i)
file.close()