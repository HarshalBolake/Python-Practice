import json

data = {"name" : "Harshal", "age" : 22, "course": "Msc Software Engineering", "skills":["Python","SQL"]}

text = json.dumps(data, indent= 2)
# print(text)

raw = '{"name" : "Harshal", "age" : 22, "course": "Msc Software Engineering","skills":["Python","SQL"]}'
obj = json.loads(raw)
# print(obj["name"])

# with open("data.json","w") as f:
#     json.dump(data,f,indent=2)

with open("backend/json/data.json") as f:
    data = json.load(f)
print(data["skills"])





