lstring = int("101000",2)
rstring = int("110000",2)
print(lstring)
print(rstring)

bitand = bin(lstring & rstring).count("1")
print(bitand) 