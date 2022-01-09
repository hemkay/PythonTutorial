import questionary

#instantiate student dictionary
students = {}

stop = False
while not stop:
    # collect name from user
    name = input("Student Name: ")

    # collect student score
    score = input("Student Score: ")

    # print("Student name is ", name)
    # print(type(name))
    # print("Student Score is ", score)
    # print(type(score))

    # cast score to float
    score = float(score)
    # print(type(score))

    students[name] = score
    
    # check if user want to add more students
    ask = questionary.confirm("Will you like to add another student? ").ask()
    if not ask:
        stop = True

    

print(students)


