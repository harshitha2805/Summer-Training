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
#To find middle number of linked list       
    '''
    def middle(self):
        c=0
        i=0
        t=self.head
        while(t!=None):
            c=c+1
            t=t.next
        c=c//2
        t=self.head
        for i in range(c):
            t=t.next
        print(t.data)
    '''
    def middle(self):
        f=self.head
        s=self.head
        while(f!=None and f.next!=None):
            s=s.next
            f=f.next.next
        print(s.data)
l1=sll()
l1.head=node(10)
l1.addback(20)
l1.addback(30)
l1.addback(40)
l1.addback(60)
l1.addback(70)
l1.addback(80)
l1.display()
print()
l1.middle()
    
