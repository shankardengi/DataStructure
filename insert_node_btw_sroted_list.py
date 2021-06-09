class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    @staticmethod
    def create_list(n):
        first = None
        cur = None
        for i in range(n):
            data = int(input("Enter Data in List:"))
            node = Node(data)
            if first == None:
                first = node
                cur = node
            else:
                cur.next = node
                cur = node
        return first

    @staticmethod
    def display(first):
        if first == None:
            print("list is empty")
        else:
            cur = first
            while cur != None:
                print("list data is :",cur.data)
                cur = cur.next

    @staticmethod
    def insert_node_btw(first):
        data  = int(input("Enter data to insert into list:"))
        node = Node(data)
        if first == None:
            print("list is empty")
        else:
            if first.data > node.data:
                node.next = first
                first = node
            else:
                prev = first
                cur = first.next
                while cur != None and cur.data < node.data:
                    prev = cur
                    cur = cur.next
                if cur == None:
                    prev.next = node
                else:
                    node.next = cur
                    prev.next = node
        return first

if __name__ == "__main__":
    n = int(input('Enter size of list:'))
    first = Node.create_list(n)
    Node.display(first)
    first = Node.insert_node_btw(first)
    Node.display(first)
