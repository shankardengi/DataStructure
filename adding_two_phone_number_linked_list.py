class Node:
    def __init__(self,data):
        self.data = int(data)
        self.next = None
    @staticmethod
    def create_list(number):
        first = None
        cur = None
        for num in number:
            node = Node(num)
            if first == None:
                first = node
                cur = node
            else:
                cur.next = node
                cur = node
        return first
    @staticmethod
    def reverse_list(first):
        if first == None:
            print("list is empty")
        else:
            if first.next == None:
                return first
            else:
                prev = first
                cur = first.next
                post = cur.next
                while cur != None:
                    cur.next = prev
                    prev = cur
                    cur = post
                    if post != None:
                        post = post.next
                first.next = None
                first = prev
        return first

    @staticmethod
    def display(first):
        cur = first
        if first == None:
            print("list is empty")
        else:
            while cur!=None:
                print("data is :",cur.data)
                cur = cur.next

    @staticmethod
    def add_list(first,second):
        carry = 0
        cur1 = first
        cur2 = second
        cur3 = None
        third = None
        while cur1 != None or cur2 != None or carry != 0:
            if cur1 != None and cur2 != None:
                data = cur1.data + cur2.data + carry
                cur1 = cur1.next
                cur2 = cur2.next
            elif cur1!=None:
                data = cur1.data + carry
                cur1 = cur1.next
            elif cur2!=None:
                data = cur2.data + carry
                cur2 = cur2.next
            else:
                data = carry
            carry = data // 10
            cur3 = Node(data % 10)
            cur3.next = third
            third = cur3

        return third

if __name__ == "__main__":
    list1 = input("Enter 1st phone nuber to add:")
    first_list = Node.create_list(list1)
    print("list 1 data is:")
    Node.display(first_list)
    list2 = input("Enter 2nd phone number to add:")
    second_list = Node.create_list(list2)
    print("list 2 data is")
    Node.display(second_list)
    first_list = Node.reverse_list(first_list)
    second_list = Node.reverse_list(second_list)
    print("added result of number is :")
    third = Node.add_list(first_list,second_list)
    Node.display(third)









