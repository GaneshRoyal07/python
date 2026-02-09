#creat an array
arr=[1,2,3,4,5]
print(arr)

#access array element
arr=[12,11,4,9,10]
print(arr[0])
print(arr[2])

#print array using for loop
arr=[1,2,3,4,5]
for i in arr:
    print(i)

#print array using index(for loop)
arr=[10,5,16,2,33]
for i in range(len(arr)):
    print(arr[i],end=" ")

#print array in reverse order
arr=[1,2,3,4,5,6]
for i in range(len(arr)-1,-1,-1):
    print(arr[i])
    
#sum of array element
arr=[10,20,30,40]
total=0
for i in arr:
    total+=i
    print(total)

#finding largest element
arr=[3,7,5,10,8]
largest=arr[0]
for i  in arr:
    if i>largest:
        largest=i
print(largest)

#count even numbers in array
arr=[1,2,3,4,5,6]
count=0
for i in arr:
    if i%2==0:
        count+=1
print(count)

#count even numbers in array
arr=[1,2,3,4,5,6]
count=0
for i in arr:
    if i%2!=0:
        count+=1
print(count)

#print even numbers
arr=[1,2,3,4,5,6,7,8,9]
for i in range(len(arr)):
    if i%2==0:
        print(i)

#print odd numbers
arr=[1,2,3,4,5,6,7,8]
for i in range(len(arr)):
    if i%2!=0:
        print(i)

#add elements to array
arr=[1,2,3,4]
arr.append(5)
print(arr)

#remove element at specified position
arr=[1,2,3,4,5]
arr.pop(0)
print(arr)

#remove element from array
arr=[1,2,3,4,5]
arr.remove(3)
print(arr)

#sort the elements
arr=[2,5,7,1,10,8,3]
arr.sort()
print(arr)

#length of the array
arr=[1,2,3,4,5]
arr=len(arr)
print(arr)