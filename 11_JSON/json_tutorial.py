import json

# python object to json 
# json object to python object == deserialization or decoding
person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

personJSON = json.dumps(person, indent=4, sort_keys=True)
print(personJSON)

with open('person.json', 'w') as file:
    json.dump(person, file, indent=4)