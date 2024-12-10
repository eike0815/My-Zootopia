import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animal_data.json')

output = ''
for fox in range(len(animals_data)):
    try:
        output += f"Name : {animals_data[fox]['name']}\n"
    except KeyError:
        pass
    try:
        output += f"Diet : {animals_data[fox]['characteristics']['diet']}\n"
    except KeyError:
        pass
    try: #hier alle hinter location sonderdingens für kommatar überlegen
        lieus = ""
        for lieu in range(0,len(animals_data[fox]['locations'])):
            lieus += animals_data[fox]['locations'][lieu]+" "
        output += f"Location: {lieus}\n"
    except KeyError:
        pass
    try:
        output += f"Type : {animals_data[fox]['characteristics']['type']}\n"
    except KeyError:
        pass
    output += "\n"

print(output)