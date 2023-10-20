class node:
    def __init__(self,z):
        self.data=z
        self.next=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
        self.tail=None
    def add_front(self,x):
        if(self.head==None):
            self.head=node(x)
            self.tail=self.head
        else:
            temp=node(x)
            temp.next=self.head
            self.head.prev=temp
            self.head=temp
    def add_end(self,x):
        if(self.head==None):
            self.head=node(x)
            self.tail=self.head
        else:
            temp=node(x)
            temp.prev=self.tail
            self.tail.next=temp
            self.tail=temp
    def delete_beg(self):
        if self.head==None:
            return
        self.head=self.head.next
        self.head.prev=None
    def delete_end(self):
        if self.head==None:
            return
        self.tail=self.tail.prev
        self.tail.next=None
    def traversal(self):
        temp=self.head
        while(temp):
            print(temp.data,end="-->")
            temp=temp.next
a=dll()
a.add_front(10)
a.add_front(20)
a.add_front(30)
a.add_end(40)
a.delete_beg()
a.delete_end()
a.traversal()