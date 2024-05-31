# Stack implementation in python

stack = []
max_size = int(input("Enter the size of the stack: "))
top = -1

while True:
    print("------MENU-------")
    print("1. Push")
    print("2. Pop")
    print("3. StackTop")
    print("4. Display")
    print("5. Exit")
    choice = int(input("Enter your choice: "))


    if choice == 1:
        if(len(stack) == max_size):
            print("Stack Overflow.")       
        else:
            val = input("Enter the value: ")
            stack.append(val)
            print('Stack after elements are pushed:', stack)
    
    elif choice == 2:
        if(len(stack) == 0):
            print("Stack is empty.")
        else:
            stack.pop()
            print('Stack after elements are popped:', stack)
            print("Popped element is: ", stack[top])
    
    elif choice == 3:
        if(len(stack) == -1):
            print("Stack Underflow")
        else:
            print("Element at top is: ", stack[top]);
    
    elif choice == 4:
        if(len(stack) == 0):
            print("Stack is empty.")
        for i in stack:
            print("The stack elements are: ", i)

    elif choice == 5:
        print("Exit Point")

    else:
        print("Invalid choice.")
        print()    
