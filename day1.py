
#python variables

x=4
y="John"
print(x,y)

x=5
x="John"
print(x)

#variable names

myVariableName="Hii"  #camel case
print(myVariableName)

MyVariableName="How Are You" #pascal case
print(MyVariableName)

my_variable_name="I'm Good" #snake case
print(my_variable_name)

#Assign multiple values
x,y,z="Orange","Apple","Banana" #many values to multiple variables
print(x)
print(y)
print(z)

x=y=z="Grapes" #one value to multiple variables
print(x)
print(y)
print(z)

fruits=["Orange","Apple","banana"] #Unpack a Collection
x,y,z=fruits
print(x)
print(y)
print(z)

#Global Variable
x="awesome"
def myfunction():
    print("Python is",x)
myfunction()

x="awesome"
def myfunc():
    x="fantastic"
    print("Python is",x)
myfunc()
print("Python is",x)

#global keyword
def myfunc():
    global x
    x="fantastic"
myfunc()
print("Python is",x)

#python list
thislist = ["apple", "banana", "cherry"]
print(thislist)

#allow duplicates
thislist=["apple","banana","apple","cherry"]
print(thislist)

#list length
thislist=["apple","banana","apple","cherry"]
print(len(thislist))

#list items - datatypes
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)