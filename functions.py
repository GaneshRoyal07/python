#calling a function
def my_function():
    print("Hello from a function")
my_function()

def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9
print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

#function with return value
def add(a,b):
    return a+b
result=add(3,4)
print(result)

def get_greeting():
    return "hello python"
message=get_greeting()
print(message)

#use pass statement
def my_function():
    pass

#function with parameter
def greet(name):
    print("hello",name)
greet("Ganesh")

#types of funtions 
#built-in function
""" print()
     len()
    type()
    range()
    max()
    min() """

#user defined functions
def square(num):
    return num*num
result=square(4)
print(result)

#function with default arguments
def greet(name="user"):
    print("Hello",name)
greet()
greet("Ganesh")

#function with multiple return values
def add(a,b):
    return a+b, a-b
sum,sub=add(10,5)
print(sum,sub)

#lambda function
square=lambda x:x*x
print(square(5))

#argument functions
#positional arguments
def add(a,b):
    print(a+b)
add(10,20)

#keyword arguments
def greet(name,age):
    print(name,age)
greet(name="Ganesh",age=21)

#default arguments
def greet(name="user"):
    print("Hello",name)
greet()
greet("Ganesh")
