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
    def longsubseq(self):
        t=self.head
        max=0
        c=1
        while(t.next!=None):
            if(t.data==t.next.data-1):
                c=c+1
            else:
                if(c>max):
                    max=c
                c=1
            t=t.next
        if(c>max):
                max=c
        print(max)
            
l1=sll()
l1.head=node(1)
l1.addback(2)
l1.addback(3)
l1.addback(4)
l1.addback(7)
l1.addback(8)
l1.addback(9)
l1.addback(3)
l1.addback(4)
l1.addback(5)
l1.display()
print()
l1.longsubseq()