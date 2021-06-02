import logging

logger = logging.getLogger("linked_list")
logger.setLevel(logging.DEBUG)

format = logging.Formatter("%(asctime)s %(levelname)s %(message)s")

linked_list_file_handler = logging.FileHandler("linked_list.log")
linked_list_file_handler.setFormatter(format)

linked_list_stream_handler = logging.StreamHandler()
linked_list_stream_handler.setFormatter(format)

logger.addHandler(linked_list_stream_handler)
logger.addHandler(linked_list_file_handler)
class employee:
    start_node = None
    def __init__(self,name,id,city):
        self.name = name
        self.id = id
        self.city = city
        self.next_node = None
        logger.info("Node is created")
    def __str__(self):
        return f"employee name  {self.name} id {self.id} city {self.city}"

    def copy(self):
        emp = employee(self.name,self.id,self.city)
        return emp

    @staticmethod
    def add_node(emp):
        if employee.start_node == None:
            employee.start_node = emp
        else:
            pointer = employee.start_node
            while pointer.next_node != None:
                pointer = pointer.next_node
            pointer.next_node = emp
        logger.info("Node added succeflly")

    @staticmethod
    def delete_node(id):
        pointer = employee.start_node
        prev_pointer = pointer
        if pointer == None:
            logger.info("List does not have Node to delete")
        else:
            if pointer.id == id:
                logger.info(f"{pointer} deleted succefully")
                employee.start_node = None

            else:
                while pointer.id != id and pointer.next_node != None:
                    prev_pointer = pointer
                    pointer = pointer.next_node
                if pointer.id == id:
                    logger.info(f"{pointer} Deleted Succcefully")
                    prev_pointer.next_node = pointer.next_node

                else:
                    logger.info("Element is not present in List")

    @staticmethod
    def display_node():
        count =0
        pointer = employee.start_node

        if pointer == None:
            logger.info("List is empty")
        else:
            while pointer != None:
                count +=1
                logger.info(f"{count} node data is {pointer}")
                pointer = pointer.next_node
    @staticmethod
    def find(emp_id):
        pointer = employee.start_node
        if pointer == None:
            logger.info("List is empty")
        else:
            while pointer.id!=emp_id and pointer.next_node != None:
                pointer = pointer.next_node
            if pointer.id == emp_id:
                logger.info(f"element found and detils are {pointer}")
            else:
                logger.info("list does not have data")
    @staticmethod
    def add_node_beg(node):
        node.next_node = employee.start_node
        employee.start_node = node
        logger.info("node inserted at beganing")
    @staticmethod
    def reverse_list():
        cur = employee.start_node
        start_reverse_list = None
        if cur == None:
            logger.info("List is empty")
        else:
            while cur != None:
                #import pdb;pdb.set_trace()
                node = cur.copy()
                if start_reverse_list == None:
                    node.next_node = None
                    start_reverse_list = node
                else:
                    node.next_node = start_reverse_list
                    start_reverse_list = node
                cur = cur.next_node
        employee.start_node = start_reverse_list
        logger.info("list reversed")


if __name__ == "__main__":
    while True:
        print("1)add node at end")
        print("2)add node at begning")
        print("3)delete node")
        print("4)find node")
        print("5)display node")
        print("6)Reverse list")
        print("7)Exit")
        ch = int(input("Enter Choice:"))
        if ch == 1:
            name = input("Enter name:")
            id = input("Enter id:")
            city = input("Enter city")
            employee.add_node(employee(name,id,city))
        elif ch == 2:
            name = input("Enter name:")
            id = input("Enter id:")
            city = input("Enter city")
            employee.add_node_beg(employee(name,id,city))
        elif ch == 3:
            id = input("Enter id to delete")
            employee.delete_node(id)
        elif ch == 4:
            id = input("Enter id to search Node")
            employee.find(id)
        elif ch == 5:
            employee.display_node()
        elif ch == 6:
            logger.info("inside reverse")
            employee.reverse_list()
        elif ch == 7:
            break


