#Implementation of doubly linked list by 4 nodes
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_head(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def insert_at_position(self, data, position):
        if position <= 0:
            print("Invalid position")
            return
        new_node = Node(data)
        if position == 1 or not self.head:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            if not self.tail:
                self.tail = new_node
            return
        current = self.head
        current_position = 1
        while current_position < position - 1 and current:
            current = current.next
            current_position += 1
        if not current:
            print("Invalid position")
            return
        new_node.next = current.next
        new_node.prev = current
        current.next = new_node
        if new_node.next:
            new_node.next.prev = new_node
        if not new_node.next:
            self.tail = new_node

    def delete_at_head(self):
        if not self.head:
            print("Insufficient Memory")
            return
        temp = self.head
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        del temp

    def delete_at_tail(self):
        if not self.tail:
            print("Insufficient Memory")
            return
        temp = self.tail
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        del temp

    def delete_at_position(self, position):
        if position <= 0:
            print("Invalid position")
            return
        if not self.head:
            print("Insufficient Memory")
            return
        if position == 1:
            self.delete_at_head()
            return
        current = self.head
        current_position = 1
        while current_position < position and current:
            current = current.next
            current_position += 1
        if not current:
            print("Invalid position")
            return
        current.prev.next = current.next
        if current.next:
            current.next.prev = current.prev
        if current == self.tail:
            self.tail = current.prev
        del current

    def search(self, key):
        current = self.head
        position = 1
        while current:
            if current.data == key:
                print(f"Element {key} found at position {position}")
                return
            current = current.next
            position += 1
        print(f"Element {key} not found in the list")

    def display(self):
         current = self.tail
         print("Doubly Linked List (Backward): ", end="")
         while current is not None:
             print(current.data, " -> ", end="")
             current = current.prev
         print("NULL")

if __name__ == "__main__":
    doubly_linked_list = DoublyLinkedList()

    while True:
        print("\n*********Main Menu*********\n")
        print("Choose one option from the following list ...")
        print("\n===============================================\n")
        print("1. Insert at head\n2. Insert at tail\n3. Insert at a specific position")
        print("4. Delete at the head\n5. Delete at the tail\n6. Delete at a specific position")
        print("7. Search\n8. Display\n9. Exit\n")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = int(input("Enter data to insert at the head: "))
            doubly_linked_list.insert_at_head(data)
        elif choice == 2:
            data = int(input("Enter data to insert at the end: "))
            doubly_linked_list.insert_at_tail(data)
        elif choice == 3:
            data = int(input("Enter data to insert: "))
            position = int(input("Enter the position to insert: "))
            doubly_linked_list.insert_at_position(data, position)
        elif choice == 4:
            doubly_linked_list.delete_at_head()
        elif choice == 5:
            doubly_linked_list.delete_at_tail()
        elif choice == 6:
            position = int(input("Enter the position to delete: "))
            doubly_linked_list.delete_at_position(position)
        elif choice == 7:
            key = int(input("Enter the element to search: "))
            doubly_linked_list.search(key)
        elif choice == 8:
            doubly_linked_list.display()
        elif choice == 9:
            print("Exiting....")
            break
        else:
            print("Invalid choice.")
