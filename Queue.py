class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class Queue:
    def __init__(self):
        self.front,self.rare=None,None

    def enqueue(self,value):
        new_node= Node(value)

        if self.rare is None:
            self.front=new_node
            self.rare=new_node
        else:
            self.rare.next=new_node
            self.rare=new_node
    
    def travarse(self):
        if self.front is None:
            return print('Queue is empty')
        cur=self.front
        while cur:
            print(cur.data, end=' ')
            cur=cur.next

    def dequeue(self):
        if self.front is None:
            return 'dequeue is not possible! Queue is empty'
        self.front=self.front.next

    def _front(self):
        if self.front is None:
            return 'Queue front is empty'
        return self.front.data
    


q=Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

q.travarse()

print (q._front())
q.dequeue()
q.dequeue()
print(q._front())
q.dequeue()
q.dequeue()
q.dequeue()

q.travarse()
q.dequeue()
print(q._front())
