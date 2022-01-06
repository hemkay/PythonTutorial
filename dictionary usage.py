# create dictionary

students = {
    "Ibrahim": 2, "Ade": 23, "Ola": 80
}

print(students)

# access element
print(students["Ola"])

#add element to a dict
students["Olu"] = 67

print(students)

#modify element
students["Ibrahim"] = 72

print(students)

#delete an element
ib = students.pop("Ibrahim")

print(students)
del students["Ola"]

print(students)


