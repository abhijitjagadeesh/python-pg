class Node:
    def __init__(self, value, next = None) -> None:
        self.value = value 
        self.next = next

class LinkedList():
    def __init__(self) -> None:
        self.head = None

    def insert_node(self, value):
        new_node = Node(value)
        if self.head:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
        else:
            self.head = new_node
        
    def print_list(self):
        if not self.head:
            print(f"Nothing to print list is empty")
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next

    def pop_element_from_list(self):
        current_node = self.head
        if not current_node:
            print("Nothing to pop: Linked list is empty")
        elif current_node.next is None:
            self.head = None
            print(f"Popped {current_node.value} from the linked list")
            del current_node 
        else:
            previous_node = None
            while current_node.next is not None:
                previous_node = current_node
                current_node = current_node.next
            previous_node.next = None
            print(f"Popped {current_node.value} from the linked list")
            del current_node

    def delete_node(self, value):
        if not self.head:
            print(f"Nothing to delete Linked list is empty")
            return

        current_node = self.head
        if current_node.value == value:
            print(f"Deleting {value} from linked list")
            self.head = current_node.next
            del current_node
            return 
        
        while current_node.next is not None:
            previous_node = current_node
            current_node = current_node.next
            next_node = current_node.next
            if current_node.value == value:
                previous_node.next = next_node
                print(f"Deleting {value} from linked list")
                del current_node
                break




            


linked_list = LinkedList()
# linked_list.insert_node(3)
# linked_list.insert_node(6)
# linked_list.insert_node(9)
# linked_list.insert_node(12)
# linked_list.pop_element_from_list()
# linked_list.pop_element_from_list()
# linked_list.pop_element_from_list()
# linked_list.pop_element_from_list()
# linked_list.pop_element_from_list()
# linked_list.print_list()
linked_list.insert_node(3)
linked_list.insert_node(6)
linked_list.insert_node(9)
linked_list.insert_node(12)
# linked_list.print_list()
# linked_list.delete_node(12)
# linked_list.print_list()
linked_list.delete_node(3)
# linked_list.print_list()
linked_list.delete_node(6)
# linked_list.print_list()
linked_list.delete_node(9)
# linked_list.print_list()
linked_list.delete_node(12)
linked_list.print_list()
# linked_list.delete_node(12)
# linked_list.print_list()