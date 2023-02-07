import json

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User('Max', 27)

# # custom encoding function
# def encode_user(o):
#     if isinstance(o, User):
#         return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
#     else:
#         raise TypeError('Object of type User is not JSON serializable')

from json import JSONEncoder

class UserEncoder(JSONEncoder):
    # override default
    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self,o)

# one way
# userJSON = json.dumps(user, cls=UserEncoder)

# second way
userJSON = UserEncoder().encode(user)

print(userJSON)