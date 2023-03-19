class Node:
    def __init__(self, data, prev = None, next = None):
        self.prev = prev
        self.data = data
        self.next = next

class NodeManager:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head

    def insert(self, data):
         if self.head == None:
            self.head = Node(data)
            self.tail = self.head
         else:
            node = self.head
            while node.next:
                node = node.next
            new = Node(data)
            node.next = new
            new.prev = node
            self.tail = new

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def search_from_head(self, data):
        if self.head == None:
            return False
        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.next
        return False

    def search_from_tail(self, data):
        if self.head == None:
            return False
        node = self.tail 
        while node:
            if node.data == data:
                return node
            else:
                node = node.prev
        return False

    def insert_before(self, data, before_data):
        if self.head == None:
            self.head = Node(data)
            return True
        else:
            node = self.tail
            while node.data != before_data:
                node = node.prev
                if node == None:
                    return False
            new = Node(data)
            before_new = node.prev
            before_new.next = new
            new.prev = before_new
            new.next = node
            node.prev = new
            return True

    def insert_after(self, data, after_data):
        if self.head == None:
            self.head = Node(data)
            return True
        else:
            node = self.head
            while node.data != after_data:
                node = node.next
                if node == None:
                    return False
            new = Node(data)
            after_new = node.next
            new.prev = node
            new.next = after_new
            after_new.prev = new
            node.next = new
            return True
    

double_linked_list = NodeManager(0)
for data in range(1, 10):
    double_linked_list.insert(data)
double_linked_list.desc() # 0,1,2,3,4,5,6,7,8,9

node_3 = double_linked_list.search_from_head(3)
if node_3 :
    print(node_3.data) # 3 검색 속도가 아래보다 더 빠름
else:
    print("No Search Data")

node_tail_3 = double_linked_list.search_from_tail(3)

if node_tail_3:
    print(node_tail_3.data) # 3 검색 속도가 위보다 더 느림
else:
    print("No Search Data")

double_linked_list.insert_before(1.5, 2)
double_linked_list.desc() # 0,1,1.5,2,3,4,5,6,7,8,9

double_linked_list.insert_after(8.5, 8)
double_linked_list.desc() 