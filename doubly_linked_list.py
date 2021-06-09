class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
    @staticmethod
    def insert_node_front(first):
        data = int(input("Enter Data into node:"))
        node = Node(data)
        if first == None:
            first = node
        else:
             first.prev = node
             node.next = first
             first = node
        return first
    @staticmethod
    def insert_node_rear(first):
        data = int(input("Enter Data into node:"))
        node = Node(data)
        if first == None:
            first = node
        else:
            cur = first
            while cur.next != None:
                cur = cur.next

            node.prev = cur
            cur.next = node
        return first

    @staticmethod
    def display(first):
        if first == None:
            print("Node is empty")
        else:
            cur = first
            while cur != None:
                print("Node data is :",cur.data)
                cur = cur.next
    @staticmethod
    def display_node(node):
        print(node.data)

    @staticmethod
    def move_node_back(cur,first):
        if first == None:
            print("list is empty")
        else:
            if cur == None:
                cur = first
            if cur.prev == None:
                print("list dont have data at backward")
            else:
                cur = cur.prev
                print("Data after moving backward")
                Node.display_node(cur)
        return cur

    @staticmethod
    def move_node_next(cur,first):
        if first == None:
            print("list is empty")
        else:
            if cur == None:
                cur = first
            if cur.next == None:
                print("list dont have element at next position")
            else:
                cur = cur.next
                print("Data after moving in forward")
                Node.display_node(cur)
        return cur

if __name__ == "__main__":
    first = None
    cur = None
    while True:
        print("1)insert node at front:")
        print("2)insert node at rear:")
        print("3)display list:")
        print("4)move node in  backward direction:")
        print("5)move node in forward direction:")
        print("6)exit:")
        ch = int(input("Enter choice:"))
        if ch == 1:
            first = Node.insert_node_front(first)
        elif ch==2:
            first = Node.insert_node_rear(first)
        elif ch == 3:
            Node.display(first)
        elif ch == 4:
            cur = Node.move_node_back(cur,first)
        elif ch == 5:
            cur = Node.move_node_next(cur,first)
        elif ch == 6:
            break

