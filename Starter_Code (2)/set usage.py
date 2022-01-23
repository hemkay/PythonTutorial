#create set
a = set([1,4,1,2,3,1])
b = {1,2,3,4,5}

c = {"abc"}
print(c)
print(a, b)

#add element
a.add(5)
print(a)

#remove element
a.remove(2)
print(a)


#access element
#print(a[2])

# set union
d = a.union(b)
print(d)

#intersection
e = a.intersection(b)
print(e)

