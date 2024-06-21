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
        print()
    def addback(self,x):
        t=self.head
        while(t.next!=None):
            t=t.next
        t.next=node(x)
    def rev(self):
        t=self.head
        t1=t.next
        t.next=None
        while(t.next!=None):
            
            t2=t.next.next
            while(t2!=None):
                print(t.data,t1.data)
                t1=t1.next   
            t=t.next 
        
l1=sll()
l1.head=node(9)
l1.addback(8)
l1.addback(5)
l1.addback(4)
l1.display()