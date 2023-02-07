import json

# # json object to python object == deserialization or decoding


with open('person.json', 'r') as file:
    person = json.load(file)
    print(person)