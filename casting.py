# casting string to int
a  = "123"
a_int = int(a)
print(type(a))
print(type(a_int))

# casting string to float

b = "1.234"
b_float = float(b)
print(type(b))
print(type(b_float))

# convert alphanumeric to int error
#c = "qwe123"
#c_int = int(c)
#print(c_int)


d = "qwe12"
print(d.isnumeric())
e = "123"
print(e.isnumeric())


# casting int to string
g = 1234
f = str(a)
print(type(g))
print(type(f))