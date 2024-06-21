#Print all possible pairs of list
'''
ip: 6 7 4 8 4 2 0 1
op: 67
6 4
6 8
6 4
6 2
6 0
6 1
7 4
7 8
7 4
7 2
7 0
7 1
4 8
4 4
4 2
4 0
4 1
8 4
8 2
8 0
8 1
4 2
4 0
4 1
2 0
2 1
0 1
'''
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
    def allpairs(self):
        t=self.head
        while(t.next!=None):
            t1=t.next
            while(t1!=None):
                print(t.data,t1.data)
                t1=t1.next   
            t=t.next 
l1=sll()
l1.head=node(6)
l1.addback(7)
l1.addback(4)
l1.addback(8)
l1.addback(4)
l1.addback(2)
l1.addback(0)
l1.addback(1)
l1.display()
l1.allpairs()