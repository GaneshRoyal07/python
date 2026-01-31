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

#arithmetic operators
a=2
b=3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
print(a//b)

#relational operators
a=10
b=5
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

#assignment operator
a=10
a+=5
print(a)
a=10
a-=5
print(a)
a=10
a*=5
print(a)
a=10
a/=5
print(a)
a=10
a//=5
print(a)
a=10
a**=5
print(a)
a=10
a%=5
print(a)
a=10
a&=5
print(a)
a=10
a|=5
print(a)
a=10
a^=5
print(a)
a=10
a<<=5
print(a)
a=10
a>>=5
print(a)

#logical operators
a=True 
b=False
print(a and b)
print( a or b)
print(not a)

#bitwise operators
a=5
b=3
print(a&b)

#membership operators
my_list=[1,2,3,4,5]
print(2 in my_list)
print(10 in my_list)
print(7 not in my_list)

#identity operators 
a=[1,2,3]
b=a
c=[1,2,3]
print(a is b)
print(a is c)
print(a is not c)

#ternary operator 
age=18
vote_status= "Can Vote" if age>=18 else "Cannot Vote"
print(vote_status)

#if statement
a=15
b=10
if a>b:
    print("a is greaterthan b")

#if and else statement
a=10
b=7
if a < b:
    print("a is lessthan b")
else:
    print("a is greaterthan b")

n= 23
if n%2==0:
    print("even")
else:
    print("odd")

#nested if statement
matches_won=10
goals=22
if matches_won>8:
    if goals>20:
        print("Hurray")
    print("Winning")