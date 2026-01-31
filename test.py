print("hello world")

a= "hlo" #string datatype
b="world"
c=a+" "+b #string concatenation
print(c)

a=15 #integer datatype
b=10
c=a+b
d=a-b
e=a*b
f=a/b
g=a%b
print(a,b,c,d,e,f,g)

a=1.5   #float datatype
b=1.5
c=a+b
d=a-b
e=a*b
f=a/b
g=a%b
print(a,b,c,d,e,f,g)

a=10 
b=15
c=a>b   #boolean datatype
d=a<b
e=a>=b
f=a<=b
g=a!=c
h=a==b
print(a,b,c,d,e,f,g,h)

#BODMAS rule
a=(5+5)*(5-1)
b=10/(1+4)
print(a,b)


#string repetition
a="*"*10
print(a)

a="string"
b="123"+"***"+a+"###"+"321"
print(b)

#length of string
a="Ganesh"
b=len(a)
print(b)

#string indexing  #indexing start with num 0
a="Ganesh"
b=a[0]+a[1]
print(b)
b=a[0:]  #string slicing
print(b)
b=a[2:5]   
print(b)

#how to check types

a="hi"
b=type(a)
print(b)

a=7
print(type(a))

a=1.7
print(type(a))

a=5>6
print(type(a))

#perameter of rectangle

a=int(4)
b=int(3)
c=2+(a*b)
print(c)

#part of string
a="Hi Ganesh"
b=3
print(a[b:])