class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

    @staticmethod
    def create_list(n):
        first = None
        cur = None
        for i in range(n):
            data = int(input("Enter Data into list:"))
            node = Node(data)
            if first == None:
                first = node
                cur = first
            else:
                node.prev = cur
                cur.next = node
                cur = node
        return first
    @staticmethod
    def display(first):
        cur = first
        if first == None:
            print("List is empty")
        print("--------------------data of linked list node is-------------------")
        while cur!= None:
            print(f"Node data is {cur.data}")
            cur = cur.next

    @staticmethod
    def insert_node_at_position(first,position):
        count = 1
        data = int(input("Enter Data:"))
        node = Node(data)
        if first == None:
            print("List is Empty")
        else:
            cur = first
            while cur.next != None and count < position:
                cur = cur.next
                count += 1
            if cur.prev == None:
                first = node
                node.next = cur
                cur.prev = node
            elif cur.next != None or count == position:
                node.prev = cur.prev
                node.next = cur
                cur.prev.next = node
                cur.prev = node
            else:
                cur.next = node
                node.prev = cur

        return first
    @staticmethod
    def delete_front(first):
        if first == None:
            print("list is empty")
        else:
            if first.next == None:
                first = None
            else:
                print("Deleted Element is :",first.data)
                first.next.prev = None
                first = first.next
        return first

    @staticmethod
    def delete_rear(first):
        cur = first
        if first == None:
            print("list is empty")
        else:
            while cur.next !=None:
                cur = cur.next
            print("Deleted node is:",cur.data)
            if cur != first:
                cur.prev.next = None
            else:
                first = cur.next
        return first

    @staticmethod
    def delete_any_node(first,position):
        count = 1
        cur = first
        if first == None:
            print("list is empty")
        else:
            while cur!=None and count < position:
                cur = cur.next
                count += 1
            if cur == None:
                print("Invalid postion to delete")
            elif cur == first:
                print("Deleted Elemnt is:",cur.data)
                first = first.next
            else:
                print("Deleted Elemnt is:",cur.data)
                cur.prev.next = cur.next
                if cur.next != None:
                    cur.next.prev = cur.prev
        return  first

    @staticmethod
    def delete_multiple_node(first,data):
        if first == None:
            print("Node is empty")
        else:
            cur = first
            while cur != None:
                if cur.data == data:
                    if cur == first:
                        first = cur.next
                        cur = first
                    else:
                        cur.prev.next = cur.next
                        if cur.next != None:
                            cur.next.prev = cur.prev
                else:
                    cur = cur.next
        return first


if __name__ == "__main__":
    n = int(input("Enter size of linked list:"))
    first = Node.create_list(n)
    Node.display(first)
    while True:
        print("1)Enter node at specific position:")
        print("2)Delete node from front")
        print("3)Delete Element from back")
        print("4)Delete Any node from list")
        print("5)Delete Multiple data from list")
        print("6)Display List")
        print("7)Exit")
        ch = int(input("Enter your choice:"))
        if ch==1:
            postition = int(input("Enter position of node to insert data:"))
            first = Node.insert_node_at_position(first, postition)
        elif ch==2:
            first = Node.delete_front(first)
        elif ch==3:
            first = Node.delete_rear(first)
        elif ch==4:
            postition = int(input("Enter position of node to Delete :"))
            first = Node.delete_any_node(first, postition)
        elif ch==5:
            postition = int(input("Enter Data to delete muliple similar node :"))
            first = Node.delete_multiple_node(first, postition)
        elif ch==6:
            Node.display(first)
        elif ch==7:
            break









