
import json
x = '{"name":"Bolatito", "age":45, "year":2003, "location":"Oyo"}'
#To change json to dict
a = json.loads(x)
print(a)
print(a["age"])
age = a["age"]
print(age)
print(a["location"])
m = json.dumps(a)
print(m)
print(type(m))
print(m["age"])


"""
#import json
x = {
    "name" : "Hammad",
    "school" : "Anwar",
    "age" : 15
    }
#To change dict to json
y = json.dumps(x)
print(y)
"""

