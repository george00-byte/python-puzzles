l = [1,2,"3","45"]
t=(1,2,34,5,56)
s= {1,2,34,45}
d= {1:"Here",2:"there",3:"three"}


for i in t:
    print(i)
print("\n")
for i in l:
    print(i)

t2=(1,2,3,45,5)
t=t.__add__(t2)
print(t[:])


l= l+["adsd",4,5]



print("\n")
l.sort( )
l.reverse()

l.append("Here")

print(l[:4])

print(l[::-1])

print("\n")



s.update({'w e',45})
print("This is a set ",s)

print("\n")


d['last'] = "value"
d.update({"23":"e" })
d.pop(1)


print("This is a dictionary",d)