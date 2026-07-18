import json

students = {
    "student1":{
        "name" : "Harshal",
        "age": 23
    },
    "student2":{
        "name":"John",
        "age": 22
    }
}

# python -> json
json_data = json.dumps(students)

# print(json_data)

# json -> python
student = json.loads(json_data)
# print(student)

# save in file
with open("students.json","w") as file:
    json.dump(students,file)

# read json file
with open("json/students.json","r") as file:
    data = json.load(file)
print(data)



