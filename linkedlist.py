class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def print(self):
        curr = self.head
        while curr:
            print(curr.data, end=' ')
            curr = curr.next

    def pushFront(self, data):
        #khoi tao node ,gan data , gan link
        newNode = Node(data)
        newNode.next = self.head
        #gan node moi vao ll
        self.head = newNode
        self.size += 1
def pushFront(self, data):#+

    newNode = Node(data)#+
    newNode.next = self.head#+
#+
    # Update the head of the linked list to the new node#+
    self.head = newNode#+
#+
    # Increment the size of the linked list#+
    self.size += 1#+
    def pushBack(self, data):
        #tao node
        newNode = Node(data)
        #neu danh sach rong
        if not self.head:
            self.head = newNode
            self.size = 1
            return
        #neu khong rong
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = newNode
        self.size += 1

def insert(self, data, k):
        #neu k khong hop le 
        if k < 0 or k > self.size:
            return
        #k =0 (head)
        if k == 0:
            self.pushFront(data)
            return
        #neu k hop le
        curr=self.head
        for i in range(1,k-1):
            curr=curr.next
        newNode=Node(data)
        tmp=curr.next.next
        curr.next=newNode
        newNode.next=tmp
        self.size-=1
if __name__=="__main__":
    ll=LinkedList()
    ll.pushFront(2)
    ll.pushFront(6)
    ll.pushFront(4)
    ll.pushFront(5)
