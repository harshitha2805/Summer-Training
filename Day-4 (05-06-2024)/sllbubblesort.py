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
    def bubsort(self):
        T=self.head
        c=0
        p=None
        while(T.next!=None):
            f=0
            t=self.head
            while(t.next!=p):
                if (t.data>t.next.data):
                    f=1
                    t.data,t.next.data=t.next.data,t.data
                t=t.next
                c=c+1
            return c
            if(f==0):
                break
            p=t
            T=T.next
            
l1=sll()
l1.head=node(6)
l1.addback(7)
l1.addback(4)
l1.addback(8)
l1.addback(5)
l1.addback(2)
l1.addback(0)
l1.addback(1)
l1.display()
b=l1.bubsort()
l1.display()
print(b)