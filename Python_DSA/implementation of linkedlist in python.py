#Implementation of linked list in python

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def count(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def traverse(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def insert_after(self, target, data):
        new_node = Node(data)
        current = self.head
        while current:
            if current.data == target:
                new_node.next = current.next
                current.next = new_node
                break
            current = current.next

    def insert_before(self, target, data):
        new_node = Node(data)
        if self.head.data == target:
            new_node.next = self.head
            self.head = new_node
        else:
            prev = None
            current = self.head
            while current:
                if current.data == target:
                    new_node.next = current
                    prev.next = new_node
                    break
                prev = current
                current = current.next

    def delete_node(self, target):
        if self.head.data == target:
            self.head = self.head.next
        else:
            prev = None
            current = self.head
            while current:
                if current.data == target:
                    prev.next = current.next
                    break
                prev = current
                current = current.next

    def destroy_list(self):
        self.head = None

if __name__ == "__main__":
    linked_list = LinkedList()

    while True:
        print("\nOperations:")
        print("1. Append")
        print("2. Display")
        print("3. Count")
        print("4. Insert After")
        print("5. Insert Before")
        print("6. Delete Node")
        print("7. Destroy List")
        print("8. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            data = input("Enter an element to append: ")
            if data.isdigit():
                data = int(data)
                linked_list.append(data)
            else:
                print("Invalid input. Please enter an integer.")

        elif choice == '2':
            print("\nLinked List:")
            linked_list.traverse()

        elif choice == '3':
            count = linked_list.count()
            print(f"Number of elements in the linked list: {count}")

        elif choice == '4':
            target = input("Enter the target element after which to insert: ")
            data = input("Enter the element to insert: ")
            if target.isdigit() and data.isdigit():
                target = int(target)
                data = int(data)
                linked_list.insert_after(target, data)
            else:
                print("Invalid input. Please enter integers.")

        elif choice == '5':
            target = input("Enter the target element before which to insert: ")
            data = input("Enter the element to insert: ")
            if target.isdigit() and data.isdigit():
                target = int(target)
                data = int(data)
                linked_list.insert_before(target, data)
            else:
                print("Invalid input. Please enter integers.")

        elif choice == '6':
            target = input("Enter the element to delete: ")
            if target.isdigit():
                target = int(target)
                linked_list.delete_node(target)
            else:
                print("Invalid input. Please enter an integer.")

        elif choice == '7':
            linked_list.destroy_list()
            print("Linked list destroyed.")

        elif choice == '8':
            break

        else:
            print("Invalid choice. Please enter a valid option.")
