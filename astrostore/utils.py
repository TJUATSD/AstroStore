import json 

def parse_config(filename) -> dict:
    with open(filename, 'r+') as f:
        data = json.loads(f.read())
        return (data['retional'], data['noretional'])