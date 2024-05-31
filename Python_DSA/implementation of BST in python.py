class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def deleteNode(root, key):
    if root is None:
        return root
    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif key > root.key:
        root.right = deleteNode(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            return temp
        elif root.right is None:
            temp = root.left
            return temp
        temp = minValueNode(root.right)
        root.key = temp.key
        root.right = deleteNode(root.right, temp.key)
    return root

def inorderTraversal(root):
    if root:
        inorderTraversal(root.left)
        print(root.key, end=' ')
        inorderTraversal(root.right)

root = None

while True:
    print("\nBinary Search Tree Operations")
    print("1. Insert")
    print("2. Delete")
    print("3. In-order Traversal")
    print("4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter the value to insert: "))
        root = insert(root, data)
    elif choice == 2:
        data = int(input("Enter the value to delete: "))
        root = deleteNode(root, data)
    elif choice == 3:
        print("In-order Traversal:", end=' ')
        inorderTraversal(root)
        print()
    elif choice == 4:
        break
    else:
        print("Invalid choice. Please try again.")
