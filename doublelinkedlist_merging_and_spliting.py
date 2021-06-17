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
            data = int(input("Enter Data to list:"))
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
        if first == None:
            print("list is empty")
        else:
            cur = first
            while cur != None:
                print("Data is :",cur.data)
                cur = cur.next
    @staticmethod
    def merge_list(first,second):
        if first == None:
            return second
        elif second == None:
            return first
        else:
            cur = first
            while cur.next!= None:
                cur = cur.next
            cur.next = second
            second.prev = cur
        return first
    @staticmethod
    def split_list(first,positon):
        #import pdb;pdb.set_trace()
        second = None
        if first == None:
            print("list is empty")
        else:
            count = 1
            cur = first
            while cur != None and count != positon:
                cur = cur.next
                count += 1
            if cur != None:
                second = cur
                cur.prev.next = None
                second.prev = None

        return (first,second)


if __name__ == "__main__":
    n = int(input("Enter size of list1:"))
    first = Node.create_list(n)
    n = int(input("Enter size of list2:"))
    second = Node.create_list(n)
    Node.display(first)
    merged_header = Node.merge_list(first,second)
    Node.display(merged_header)
    position = int(input("Enter split position:"))
    first,second = Node.split_list(merged_header,position)
    print("Splited first list")
    Node.display(first)
    print("Splited second list")
    Node.display(second)




