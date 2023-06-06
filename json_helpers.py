import json


def readJsonData(file_path):
    with open(file_path, "r") as file:
        return json.load(file)


def saveToJsonFile(key, object, filename):
    json_obj = json.dumps({key: object})
    with open(filename, "w") as outfile:
        outfile.write(json_obj)
