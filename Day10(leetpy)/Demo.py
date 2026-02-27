# class Node:
#     def __init__(self, data):  
#         self.data = data       
#         self.next = None

# # Creating nodes
# n1 = Node(10)
# n2 = Node(20)
# n3 = Node(30)  

# # Linking nodes
# n1.next = n2
# n2.next = n3

# # Printing values
# print(n1.data)
# print(n1.next.data)

class Node:
    def __init__(self, data):
        self.data = data       
        self.next = None


class Linkedlist:
    def __init__(self):       
        self.head = None

    def insert_begin(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def insert_end(self, data):   
        endnewNode = Node(data)

        if self.head is None:
            self.head = endnewNode
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = endnewNode   

    def insert_pos(self,pos,data):
        newNode=Node(data)
        if pos==1:
            newNode.next=self.head
            self.head=newNode
            return
        temp=self.head
        for _ in range(pos-2):
            temp=temp.next
        newNode.next=temp.next
        temp.next=newNode




    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")



li = Linkedlist()
li.insert_begin(10)
li.insert_begin(5)
li.insert_begin(20)
li.insert_begin(30)
li.insert_begin(15)
li.insert_end(50)
li.display()