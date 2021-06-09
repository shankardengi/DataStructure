class Node:
    def __init__(self,rank):
        self.data = rank
        self.next = None

    @staticmethod
    def create_list(n):
        first = None
        cur = None
        for i in range(n):
            data = int(input("Enter student rank:"))
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
        else :
            cur = first
            while cur != None:
                print("Node is ",cur.data)
                cur = cur.next
    @staticmethod
    def sort_list(first):
        i = first
        if first == None:
            print("list is empty")
        else:
            while i != None:
                j = first
                while j.next != None:
                    if j.data > j.next.data:
                        temp = j.data
                        j.data = j.next.data
                        j.next.data = temp
                    j = j.next
                i = i.next
        return first

if __name__ == "__main__":
    n = int (input("Enter size list:"))
    first = Node.create_list(n)
    Node.display(first)
    first = Node.sort_list(first)
    print("Sorted List is:")
    Node.display(first)






