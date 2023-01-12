import json


def adjust_json(unformatted_json):
    #your_json = str(input('JSON: '))
    your_json = unformatted_json
    parsed = json.loads(your_json)
    return json.dumps(parsed, indent=4)
