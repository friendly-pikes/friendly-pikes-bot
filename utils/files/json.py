import platform
import json

# So we don't have to keep copying the code, have it on one file!

def get_json_file(filename):
    jsonFile = None
    filepath = "D:/Code/Discord Bots/friendly-pikes-bot/misc/"+filename+".json"

    if platform.system() == "Linux":
        filepath = f"/home/container/misc/{filename}.json"

    with open(filepath) as file:
        jsonFile = json.loads(file.read())

    return jsonFile