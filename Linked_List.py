
# This is a Singlee linked-list practice doing by Maruf

class Node:
    def __init__(self,value):
        self.data=value
        self.next= None

class Linked_List:
    def __init__(self):
        self.head=None
        self.n=0

    def len(self):
        return self.n
    
    def is_head(self, node):
        return node==self.head
    
    def is_tail(self,node):
        return node is not None and node.next is None
    
    def insert_head(self,value):
        new_node= Node(value)
        new_node.next=self.head
        self.head=new_node
        self.n+=1
    
    def travarse(self):
        cur=self.head
        while(cur!=None):
            print(cur.data, end=' ')
            cur=cur.next
        print('')


    def __str__(self):
        cur=self.head
        result=''
        while(cur!=None):
            result+=str(cur.data)+' -> '
            cur=cur.next
        return result[:-3]
    
    def append(self, value):
        new_node=Node(value)
        
        if self.head==None:
            self.head=new_node
            self.n+=1
            return
        
        cur= self.head
        while cur.next!=None:
            cur=cur.next
        cur.next=new_node
        self.n+=1

    def insert(self,after,value):
        new_node= Node(value)
        cur= self.head
        while(cur != None):
            if cur.data==after:
                break
            cur=cur.next
        if (cur != None):
            new_node.next=cur.next
            cur.next=new_node
            self.n+=1
        else: print('item not found')

    def clear(self):
        self.head=None
        self.n=0

    def delete_head(self):
        if self.head is None:
            print("Error! Empty Linked-List")
            return
        self.head=self.head.next
        self.n-=1

    def pop(self):
        if self.head is None:
            print("Error! Empty Linked-List")
            return
        cur=self.head
        if cur.next is None:
            self.delete_head()
            return
        while cur.next.next is not None:
            cur=cur.next
        
        cur.next=None
        self.n-=1

    def delete_item(self,item):
        if self.head is None:
            print("Error! Empty Linked-List")
            return
    
        cur=self.head
        if cur.data is item:
            return self.delete_head()
    
        while cur.next is not None:
            if cur.next.data is item:
                break
            cur=cur.next
              
        if cur.next is None:
            return print('item not found...!!!')
        else: cur.next=cur.next.next

    def search(self, item):
        cur=self.head
        pos=0
        while cur is not None:
            if cur.data is item:
                return print(f'item fount at position: {pos}')
            cur=cur.next
            pos+=1
        return print('item Not found')
    
    def __getitem__(self,index):
        cur=self.head
        pos=0

        while cur is not None:
            if pos is index:
                break
            cur=cur.next
            pos+=1
        if pos is not index:
            return 'Error index'
        return cur.data
    
    def find_max(self):
        if self.head is None:
            return 'empty Linked-List'
        
        cur = self.head
        mx=-1
        while cur is not None:
            if cur.data>mx:
                mx=cur.data
            cur=cur.next
        return mx
    
    def replace_max(self,value):
        if self.head is None:
            return 'empty Linked-List'
        
        mx=self.find_max()
        cur=self.head

        while cur!=None:
            if (cur.data is mx):
                cur.data=value
                break
            cur=cur.next
    
    def reverse(self):
        prev_node=None
        cur=self.head

        while cur is not None:
            next_node=cur.next
            cur.next=prev_node
            prev_node=cur
            cur=next_node

        self.head=prev_node
    
    def Change_sentance(self):
        cur= self.head
        while cur is not None:
            if cur.data == '*' or cur.data == '/':
                cur.data=' '
                if cur.next.data == '*' or cur.next.data == '/':
                    cur.next.next.data=cur.next.next.data.upper() 
                    cur.next=cur.next.next
            cur=cur.next
        

# l=Linked_List()
# l.insert_head(1)
# l.insert_head(2)
# l.insert_head(3)
# l.insert_head(4)
# l.append(5)
# # l.append(11)
# l.insert(11,32)
# l.insert(2,9)
# print (l.len())
# print(l)
# # l.travarse()
# l.clear()
# print(l)

# l.insert_head(1)
# l.insert_head(2)
# l.insert_head(3)
# l.insert_head(4)
# l.append(5)
# # l.append(11)
# l.insert(11,32)
# l.insert(2,9)
# print (l.len())
# print(l)

# l.delete_head()
# print(l)
# print(l.len())
# l.delete_item(3)
# print(l)
# l.search(8)
# print(l[8])
# print(l.find_max())
# l.replace_max(40)
# print(l)
# l.reverse()
# print(l)

s=Linked_List()
s.append('T')
s.append('h')
s.append('e')
s.append('*')
s.append('/')
s.append('s')
s.append('k')
s.append('y')
s.append('/')
s.append('i')
s.append('s')
s.append('*')
s.append('*')
s.append('b')
s.append('l')
s.append('u')
s.append('e')
s.Change_sentance()
print(s)