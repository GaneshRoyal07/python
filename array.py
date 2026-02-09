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

#find smallest element
arr=[10,22,15,7,20]
min_val=arr[0]
for i in arr:
    if i<min_val:
        min_val=i
print(min_val)

#count even and odd numbers
arr=[1,2,3,4,5,6]
even=odd=0
for i in arr:
    if i%2==0:
        even+=1
    else:
        odd+=1
print(even)
print(odd)

#check element exists in array 
arr=[10,20,30,40,50]
key=30
found=False
for i in arr:
    if i==key:
        found=True
        break
print("Found" if found else "Not Found")

#remove duplicates from array
arr=[1,2,3,3,4,5,5]
unique=[]
for i in arr:
    if i not in unique:
        unique.append(i)
print(unique)

#find second largest number
arr=[10,20,4,45,90]
first=second=-1
for i in arr:
    if i>first:
        second=first
        first=i
    elif i>second and i != first:
        second=i
print(first)
print(second)

#find duplicate elements
arr=[1,2,3,2,4,3,5]
duplicates=[]
for i in arr:
    if arr.count(i)>1 and i not in duplicates:
        duplicates.append(i)
print(duplicates)

#reverse order using for loop
num=[1,2,3,4,5]
for i in reversed(num):
    print(i)

#reverse character of a string using for loop
arr = ["python"]
s = arr[0]
for i in range(len(s) - 1, -1, -1):
    print(s[i],end="")

#reverse order of strings in the array
arr=["Python","java","c"]
for i in range(len(arr)-1,-1,-1):
    print(i)