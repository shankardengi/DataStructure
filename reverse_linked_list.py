class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    @staticmethod
    def insert_node(n):
        first = None
        prev = None
        cur = None
        for i in range(n):
            data = int(input("Enter data:"))
            node = Node(data)
            if first == None:
                first = node
                cur = first
            else:
                cur.next = node
                cur = cur.next
        return  first
    @staticmethod
    def display(first):
        cur = first
        while cur != None:
            print(cur.data)
            cur = cur.next

    @staticmethod
    def reverse_list(first):
        if first == None:
            print("list is empty")
        else:
            if first.next == None:
                print("list has one method to reverse")
                return
            else:
                prev = first
                cur = first.next
                post = cur.next
                while cur !=None or post!=None:
                    cur.next = prev
                    prev = cur
                    cur = post
                    if post != None:
                        post = post.next
                first.next = None
                first = prev
        return first




if __name__ == "__main__":
    n = int(input("Size of list:"))
    first = Node.insert_node(n)
    Node.display(first)
    first = Node.reverse_list(first)
    print("Reversed linked list is")
    Node.display(first)







