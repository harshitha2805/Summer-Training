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
#To find length of linked list is even or odd with more time complexity        
    '''
    def length(self):
        c=0
        t=self.head
        while(t!=None):
            c=c+1
            t=t.next
        if c%2==0:
            print("Even")
        else:
            print("Odd")
    '''
    def length(self):
        f=self.head
        s=self.head
        while(f!=None and f.next!=None):
            s=s.next
            f=f.next.next
        if(f==None):
            print("Even")
        else:
            print("Odd")
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
l1.length()
    