import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def serialize_animal(animal_obj):
    """ Handles serialization of a single animal object into HTML. """
    output = "" # define an empty string
    output += '<li class="cards__item">'
    output += f'<div class="card__title">{animal_obj['name']}</div>'
    output += '<p class="card__text">'
    output += f'<strong>Diet: </strong>{animal_obj['characteristics']['diet']}<br/>'
    output += f'<strong>Location: </strong>{animal_obj['locations'][0]}<br/>'

    if animal_obj['characteristics'].get('type') is None:
        output += "<br/>"
        return output

    output += f'<strong>Type: </strong>{animal_obj['characteristics'].get('type')}<br/>'
    return output


def main():
    animals_data = load_data('animals_data.json')

    output = ''
    for animal_obj in animals_data:
    # Append information to each string
        output += serialize_animal(animal_obj)


    with open ("animals_template.html", "r") as fileobj:
        html_content = fileobj.read()

    animal_info = html_content.replace("__REPLACE_ANIMALS_INFO__", output)

    with open("animals.html", "w") as fileobj:
        fileobj.write(animal_info)


if __name__ == "__main__":
    main()