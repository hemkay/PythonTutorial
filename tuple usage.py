# create a tuple
a = (1,2)
print(a)

b = 1,
print(b)

c = tuple()
print(c)

#access tuple element
print(a[1])


#change element value
#a[1] = 4

print(a)

#exception
d = (1,2 ,3 ,4, [1,2,4])
print(d)
#print(d[-1])
d[-1][2] = 6

print(d)

#d[-1] = 3
#print(d)