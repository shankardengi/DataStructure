class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    @staticmethod
    def create_list(n):
        first = None
        for i in range(n):
            data = int(input("Enter data into list"))
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
            while cur!= None:
                print("Data in node is :",cur.data)
                cur = cur.next


    @staticmethod
    def merge_list(list1,list2):
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        else:
            cur = list1
            while cur.next != None:
                cur = cur.next
            cur.next = list2
        return list1


if __name__ == "__main__":
    n = int(input("Enter size of list:"))
    first_list = Node.create_list(n)
    second_list = Node.create_list(n)
    print("first list ")
    Node.display(first_list)
    print("second list")
    Node.display(second_list)
    print("Merged List")
    merged_list = Node.merge_list(first_list,second_list)
    Node.display(merged_list)
