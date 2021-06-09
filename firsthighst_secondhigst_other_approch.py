class node:
    def __init__(self,data):
        self.data = data
        self.next = None
    @staticmethod
    def creat_list(n):
        first = None
        cur = first
        for i in range(n):
            data = int(input("Enter Data to list:"))
            nodes = node(data)
            if first == None:
                first = nodes
                cur = first
            else:
                cur.next = nodes
                cur = nodes
        return first

    @staticmethod
    def display(first):
        cur = first
        if first == None:
            print("List is empty")
        else :
            while cur != None:
                print(f"list data is {cur.data}")
                cur = cur.next
    @staticmethod
    def first_second_hig_method(first):
        if first == None:
            print("list is empty")
        else:
            cur = first
            if first.data>first.next.data:
                fh = first
                sh = first.next
            else:
                fh = first.next
                sh = first
            cur = first.next.next
            while cur != None:
                if cur.data > fh.data:
                    sh = fh
                    fh = cur
                elif cur.data > sh.data:
                    sh = cur
                cur = cur.next
        return (fh,sh)
if __name__ == "__main__":

    n = int(input("Enter size of list:"))
    first = node.creat_list(n)
    node.display(first)
    fh,sh = node.first_second_hig_method(first)
    print(f"first highst data is {fh.data} \n second highst data is {sh.data} \n")


