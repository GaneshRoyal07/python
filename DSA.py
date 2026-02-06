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

#stack using python lists
stack = []

# Push
stack.append('A')
stack.append('B')
stack.append('C')
print("Stack: ", stack)

# Peek
topElement = stack[-1]
print("Peek: ", topElement)

# Pop
poppedElement = stack.pop()
print("Pop: ", poppedElement)

# Stack after Pop
print("Stack after Pop: ", stack)

# isEmpty
isEmpty =not bool(stack)
print("isEmpty: ", isEmpty)

# Size
print("Size: ",len(stack))

#creating a stack using class
class Stack:
    def __init__(self):
       self.stack=[]
    def push(self,element):
       self.stack.append(element)
    def pop(self):
        if self.isEmpty1():
            return "Stack is Empty"
        return self.stack.pop()
    def peek1(self):
        if self.isEmpty1():
            return "Stack is Empty"
        return self.stack[-1]
    def isEmpty1(self):
       return len(self.stack)==0
    def size(self):
       return len(self.stack)
       

MyStack=Stack()
MyStack.push('X')
MyStack.push('Y')
MyStack.push('Z')

print("Stack: ",MyStack.stack)
print("Pop: ",MyStack.pop())
print("Stack after Pop: ",MyStack.stack)
print("Peek: ", MyStack.peek1())
print("isEmpty: ",MyStack.isEmpty1())
print("Length: ",MyStack.size())

#stack using linked lists
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class Stack:
    def __init__(self):
        self.head=None
        self.size=0
    def push(self,value):
        new_node=Node(value)
        if self.head:
            new_node.next=self.head
        self.head=new_node
        self.size+=1
    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        Popped_node=self.head
        self.head=self.head.next
        self.size-=1
        return Popped_node.value
    def peek(self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.head.value
    def isEmpty(self):
        return self.size==0
    def stackSize(self):
        return self.size
    def traverseAndPrint(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.value, end=" -> ")
            currentNode = currentNode.next
        print()
myStack=Stack()
myStack.push("A")
myStack.push("B")
myStack.push("C")

print("Linked List: ",end="")
myStack.traverseAndPrint()
print("Peek: ",myStack.peek())
print("Pop: ",myStack.pop())
print("Linked List after Pop: ",end="")
myStack.traverseAndPrint()
print("isEmpty: ",myStack.isEmpty())
print("Size: ",myStack.stackSize())
    
      