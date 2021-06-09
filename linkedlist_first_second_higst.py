class linked_list:
    def __init__(self,data):
        self.data = data
        self.next = None

    @staticmethod
    def create_list():
        size = int(input("size of list:"))
        first = None
        for i in range(size):
            data = linked_list(int(input("Enter Data:")))
            data.next = first
            first = data
        return first
    @staticmethod
    def display_node(pointer):
        print("list contain below data:")
        while pointer != None:
            print(f"data :{pointer.data}")
            pointer = pointer.next
    @staticmethod
    def find_higst_lowest(list1):
        #import pdb;pdb.set_trace()
        cur = list1
        first_high = None
        second_high = None
        if list1 == None:
            print("list is empty")
        else:
            while cur != None:
                if first_high == None and second_high == None:
                    if cur.data > cur.next.data:
                        first_high = cur
                        second_high = cur.next
                    else:
                        first_high = cur.next
                        second_high = cur
                    cur = cur.next.next
                else:
                    if cur.data > first_high.data:
                        second_high = first_high
                        first_high = cur

                    elif cur.data > second_high.data:
                        second_high = cur
                    cur = cur.next
        return(first_high.data,second_high.data)







if __name__ == "__main__":
    first_node = linked_list.create_list()
    linked_list.display_node(first_node)
    #second_node = linked_list.create_list()
    #linked_list.display_node(second_node)
    higst,lowest = linked_list.find_higst_lowest(first_node)
    print("higest of node is:",higst)
    print("lowest of node is:",lowest)

