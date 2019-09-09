a = "This is a string"
print (a)

tup = (1,"a","s",5+6)
print (tup)

s=[1,2,"string","a",3]
s.append(9)
print (s)
print (s[3])

a = [1,2,3,4]
b = [5,6]
a.extend(b)
print (a)


def myfun():
     x = 10
     print("value of",x) 
myfun()

def add(x=5,y=6):
 print("value",add(x,y))

