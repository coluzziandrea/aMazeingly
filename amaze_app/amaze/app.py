import sys
import json

print("Number of arguments: {}".format(len(sys.argv)))
print("Argument List: {}".format(str(sys.argv)))


with open('./scripts/input_map.json') as json_file:
    data = json.load(json_file)
    for p in data['rooms']:
        print('Name: ' + p['name'])
        print('')
