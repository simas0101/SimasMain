students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

#gryffindors = [
    #student["name"] for student in students if student["house"] == "Gryffindor"


#for gryffindor in sorted(gryffindors):
    #print(gryffindor)

#ANTRAS VARIANTAS("filter"):

#def is_gryffindor(s):
    #return s["house"] == "Gryffindor"

#gryffindors = filter(is_gryffindor, students)

#for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
    #print(gryffindor["name"])

#DICTIONARY COMPREHENSIONS:

students = ["Hermione", "Harry", "Ron"]

gryffindors = {student : "Gryffindor" for student in students}

print(gryffindors)
