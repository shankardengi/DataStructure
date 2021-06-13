#add even and odd position in singly link list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    @staticmethod
    def create_list(n):
        first = None
        cur = None
        for i in range(n):
            data = int(input("Enter data into list:"))
            node = Node(data)
            if first == None:
                first = node
                cur = first
            else:
                cur.next = node
                cur = cur.next
        return first
    @staticmethod
    def display(first):
        cur = first
        if first == None:
            print("List is empty")
        else:
            while cur != None:
                print("Node data is:",cur.data)
                cur = cur.next

    @staticmethod
    def add_even_odd_list(first):
        cur = first
        count = 1
        odd_add = 0
        even_add = 0
        while cur != None:
            if count % 2 == 0:
                even_add += cur.data
            else:
                odd_add +=cur.data
            count +=1
            cur = cur.next
        return (even_add,odd_add)

if __name__ == "__main__":
    n = int(input("Enter size of list:"))
    first = Node.create_list(n)
    print("Data in list:")
    Node.display(first)
    even_add,odd_add = Node.add_even_odd_list(first)
    print("Even sum is:",even_add)
    print("Odd sum is :",odd_add)






