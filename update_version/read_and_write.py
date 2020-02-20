
import json

def read_json(selector):
    with open('static/data.json') as json_file:

        read = json.load(json_file)
        data = read[selector]
    json_file.close()
    return(data)

def write_json(filename, data):
    with open(f'static/{filename}.json', 'w') as outfile:
        json.dump(data, outfile)

def json_parse(data):
    data = json.dumps(data)
    data = json.loads(data)
    return(data)