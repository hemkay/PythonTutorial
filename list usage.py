# list usage
names_of_students = []

#add element to the end of a list
names_of_students.append("Ibrahim")
print(names_of_students)

names_of_students.append("Olu")
print(names_of_students)

#access a list element
print(names_of_students[1])
print(names_of_students[0])
print("------negative access of list element----")
print(names_of_students[-1])
print(names_of_students[-2])


#insert element at specific position
names_of_students.insert(1, "BJ")
names_of_students.insert(2, "Oladele")
print(names_of_students)

#remove element at the end of the list
names_of_students.pop()
print(names_of_students)


#remove specific element
names_of_students.remove("BJ")

print(names_of_students)

names_of_students.append("BJ")
names_of_students.append("BJ")

names_of_students.remove("BJ")
#names_of_students.remove("AY")

print(names_of_students)


#sor list
numbers = [1,4,7,3,9]
print(numbers)
#descenidng order
numbers.sort(reverse= True)
print(numbers)

#ascending order
numbers.sort(reverse=False)
print(numbers)

#reverse list
num = [4, 1, 6, 8]
num.reverse()
print(num)

#length of a list
list_l = [1,5, "ADE", 7]
list_length = len(list_l)
print(list_length)


# count occurence of an element
user = ["ade", "ade", "ade", "ola", "bj"]
ade_count = user.count("ade")
print(ade_count)

ola_count = user.count("ola")
print(ola_count)


#change element
a = [1, 2, 3]
print(a)

a[1] = 4

print(a)


#extend
a = [1,2,3]
b = [4,5]
c = [1,2,3]
a.append(b)
print(a)
c.extend(b)
print(c)