
import json
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
def read_json(selector):
    with open('static/data.json') as json_file:

        read = json.load(json_file)
        data = read[selector]
    json_file.close()
    return(data)

def write_json(filename, data):
    
    with open(f'{dir_path}/../assets/json/{filename}.json', 'w') as outfile:
        json.dump(data, outfile)

def json_parse(data):
    data = json.dumps(data)
    data = json.loads(data)
    return(data)