#count even or odd in circular linked list
#
#create circular linked list 1)insert at front and insert at rear display
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    @staticmethod
    def insert_at_rear(first):
        #import pdb;pdb.set_trace()
        cur = first
        data = int(input("Enter data "))
        node = Node(data)
        if first == None:
            first = node
            node.next = first
            cur = first
        else:
            while cur.next != first:
                cur = cur.next
            node.next = cur.next
            cur.next = node
        return  first

    @staticmethod
    def insert_at_front(first):
        cur = first
        data = int(input("Enter data to insert at first:"))
        node = Node(data)
        if first == None:
            first = node
            node.next = first
            cur = first
        else:
            while cur.next != first:
                cur = cur.next
            cur.next = node
            node.next = first
            first = node
        return  first

    @staticmethod
    def creat_list(n):
        first = None
        cur = None
        for i in range(n):
            data = int(input("Enter data"))
            node = Node(data)
            if first == None:
                first = node
                node.next = first
                cur = first
            else:
                node.next = first
                cur.next = node
                cur = node
        return  first

    @staticmethod
    def display(first):
        #import pdb;pdb.set_trace()
        cur = first
        if first == None:
            print("List is empty")
        else:
            while cur.next != first:
                print("data in list is",cur.data)
                cur = cur.next
            print("data in list is",cur.data)
    @staticmethod
    def delete_rear(first):
        prev = None
        cur = first
        if first == None:
            print("list is empty")
        else:
            if first.next == first:
                first = None
            else:
                while cur.next != first:
                    prev = cur
                    cur = cur.next
                prev.next = cur.next
        return first
    @staticmethod
    def delete_front(first):
        if first == None:
            print("list is empty")
        else:
            cur = first
            if first.next == first:
                first = None
            else:
                while cur.next != first:
                    cur = cur.next
                cur.next = first.next
                first = first.next
        return first

    @staticmethod
    def insert_at_position(first,position):
        count = 1
        data = int(input("Enter data to list:"))
        node = Node(data)
        if first == None:
            first = node
            node.next = first
        else:
            cur = first
            prev = first
            while cur.next != first and  count != position:
                prev = cur
                cur = cur.next
                count += 1
            if cur.next == first and count != position:
                print("list dont have position so inserting node at last")
                node.next = first
                cur.next = node
            else:
                if position == 1:
                    while cur.next != first:
                        cur = cur.next
                    node.next = first
                    first  = node
                    cur.next = first
                else:
                    node.next = cur
                    prev.next = node
        return  first
    @staticmethod
    def delete_from_position(first,position):
        count = 1
        if first == None:
            print("list is empty")
        else:
            cur = first
            prev = first
            if first == first.next:
                first = None
            else:
                while cur.next != first and count != position:
                    prev = cur
                    cur = cur.next
                    count += 1
                if cur.next == first and count != position:
                    print("position not found")
                else:
                    if position == 1:
                        while cur.next != first:
                            cur = cur.next
                        first = first.next
                        cur.next = first

                    else:
                        prev.next = cur.next
        return  first



        pass
    @staticmethod
    def count_even_odd(first):
        import pdb;pdb.set_trace()
        c_even = 0
        c_odd = 0
        if first == None:
            print("list is empty")
        else:
            cur = first
            while cur.next != first:
                if cur.data % 2 == 0:
                    c_even += 1
                else:
                    c_odd += 1
                cur = cur.next
            if cur.next == first:
                if cur.data % 2 == 0:
                    c_even += 1
                else:
                    c_odd += 1

        return (c_even,c_odd)



if __name__ == "__main__":
    first = None
    while True:
        print("1)create list of circular linked list:")
        print("2)display linked linst")
        print("3)insert node  at rear")
        print("4)insert at node at front")
        print("5)delete from rear")
        print("6)delete node from front")
        print("7)insert node at position")
        print("8)count number of even and odd in list")
        print("9)delete from position")
        print("10)Exit")
        ch = int(input("Enter choice:"))
        if ch == 1:
            n = int(input("Enter size of list:"))
            first = Node.creat_list(n)
        elif ch == 2:
            Node.display(first)
        elif ch == 3:
            first = Node.insert_at_rear(first)
        elif ch == 4:
            first = Node.insert_at_front(first)
        elif ch == 5:
            first = Node.delete_rear(first)
        elif ch == 6:
            first = Node.delete_front(first)
        elif ch == 7:
            position = int(input("Enter position to insert element"))
            first = Node.insert_at_position(first,position)
        elif ch == 8:
            even,odd = Node.count_even_odd(first)
            print(f"Number of even is {even} and odd is {odd}")
        elif ch == 9:
            position = int(input("Enter position to delete element"))
            first = Node.delete_from_position(first,position)

        elif ch == 10:
            break



