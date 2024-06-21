#Binary search cannot be implemented in singly linked list because it requires indexing
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
    def addfront(self,x):
        t=node(5)
        t.next=self.head
        self.head=t
    def addback(self,x):
        t=self.head
        while(t.next!=None):
            t=t.next
        t.next=node(x)
    def addeven(self):
        t=self.head
        s=0
        while(t!=None):
            if(t.data%2==0):
                s=s+t.data
            t=t.next
        print("Even sum= ",s)
    def search(self,x):
        t=self.head
        while(t!=None):
            if t.data==x:
                return "Found"
            t=t.next
        return "Not Found"
    def middle(self):
        f=self.head
        s=self.head
        while(f!=None and f.next!=None):
            s=s.next
            f=f.next.next
        print(s.data)
    def length(self):
        f=self.head
        s=self.head
        while(f!=None and f.next!=None):
            s=s.next
            f=f.next.next
        if(f==None):
            print("Length is Even")
        else:
            print("Length is Odd")
        
l1=sll()
l1.head=node(10)
l1.addback(21)
l1.addback(30)
l1.addback(43)
l1.addback(60)
l1.addback(65)
l2=sll()
l2.head=node(100)
l2.addback(200)
l2.addback(303)
l2.addback(400)
l2.addback(519)
l2.addback(500)
l1.addfront(5)
l1.display()
print()
l2.display()
print()
l1.addeven()
l2.addeven()
print(l1.search((66)))
l1.middle()
l1.length()
    






