class Node(object):
    def __init__(self,data):
        self.data =data
        self.next=None

class SinglyLinledList(object):
    def __init__(self):
        self.head =None
        self.tail=None

    def enqueue(self,node):
        if self.head==None:
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            self.tail=self.tail.next

    def dequeue(self):
        if self.head == None:
            return -1
        v=self.head.data
        self.head=self.head.next

        if self.head == None:
            self.tail = None
        return v