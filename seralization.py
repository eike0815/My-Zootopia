"""this file is just as an working file, if i mess up sonething, i got it saved and don´t have to look for a earlier version."""
import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def seralize_animal(obj):
    output = ''
    output += '<li class ="cards__item>\n'
    try:
        output += f'<div class="card_title">{obj["name"]}</div>\n'
    except KeyError:
        pass
    output += '<p class="card__text">'
    try:
        output += f'<strong>Diet:</strong> {obj["characteristics"]["diet"]}<br/>\n'
    except KeyError:
        pass
    try:
        lieus = ""
        for lieu in range(0,len(obj["locations"])):
            lieus += obj["locations"][lieu]+" "
        output += f'<strong>Location:</strong> {lieus}<br/>\n'
    except KeyError:
        pass
    try:
        output += f'<strong>Type:</strong> {obj["characteristics"]["type"]}<br/>\n'
    except KeyError:
        pass
    output += '</p></li>'
    return output


#print(output)
animals_data = load_data('animal_data.json')
output = ""
for fox in range(len(animals_data)):
    output += seralize_animal(animals_data[fox])

print(output)