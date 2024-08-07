
class Node:
    
    def __init__(self,value):
        self.data=value
        self.next=None
    
class Stack:
    def __init__(self):
        self.top=None
        self.n=0
    
    def is_empty(self):
        return self.top==None
    
    def push(self,value):
        new_node=Node(value)
        new_node.next=self.top
        self.top=new_node
        self.n+=1

    def travarse(self):
        cur=self.top
        while cur:
            print (cur.data, end=' ')
            cur=cur.next

        print('')
    def peek(self):
        if self.is_empty():
            return print("Stack is empty")
        else:
            print(self.top.data)
    
    def pop(self):
        if self.is_empty():
            return print("Stack is empty")
        self.top=self.top.next
        self.n-=1

    def size(self):
        return print('stack size is ',self.n)

s=Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
print(s.is_empty())
s.travarse()
s.peek()
s.pop()
s.travarse()
s.size()