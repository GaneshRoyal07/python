#creating lists
x=[]
y=[1,2,3,4,5]
z=[1,"hello",3.14,True]
print(x)
print(y)
print(z)

#list methods
x=[2,5,3,1,9,4]
x.append(8)
x.sort()
print(x)

#creating algorithm
my_array=[12,4,15,6,7,9]
minVal=my_array[0]
for i in my_array:
  if i < minVal:
    minVal = i

print('Lowest value:', minVal)