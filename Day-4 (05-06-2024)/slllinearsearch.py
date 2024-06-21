#Create Linked list and search for an element in the list using linear search.
class node:
    def __init__(self,u):
        self.data=u
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def display(self):
        t=self.head
        while(t!=None):
            print(t.data,end="->")
            t=t.next
    def addback(self,x):
        t=self.head
        while(t.next!=None):
            t=t.next
        t.next=node(x)
    def search(self,x):
        t=self.head
        while(t!=None):
            if t.data==x:
                return "Found"
            t=t.next
        return "Not Found"
l1=sll()
l1.head=node(10)
l1.addback(21)
l1.addback(30)
l1.addback(43)
l1.addback(60)
l1.addback(65)
l1.display()
print()
print(l1.search((62)))



