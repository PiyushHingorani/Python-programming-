# Queue implementation in python

class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = []
        self.front = self.rear = 0

    def Enqueue(self, item):
        if(self.rear == self.size):
            print("\nQueue is full")
        else:
            self.queue.append(item)
            self.rear += 1
            print('Queue after elements are enqueued:', self.queue)          

    def Dequeue(self):
        if(self.front == self.rear):
            print("Queue is empty")
        else:
            x = self.queue.pop(0)
            self.rear -= 1
            print('Queue after elements are dequeued:', self.queue)    
        
    def Display(self):
        if(self.front == self.rear):
            print("\nQueue is Empty")
        for i in self.queue:
            print("The elements in the queue are:", i)

    def Front(self):
        if(self.front == self.rear):
            print("\nQueue is Empty")
        print("\nFront Element is:", self.queue[self.front])
        
    def Exit(self):
        print("Exit Point")

def main():
    size = int(input("Enter the size of the queue: "))
    queue = Queue(size)
    front = rear = 0

    while True:
        print("\nMenu:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Frontmost")
        print("4. Display")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            item = input("Enter the item to enqueue: ")
            queue.Enqueue(item);
        elif choice == "2":
            queue.Dequeue()
        elif choice == "3":
            queue.Front()
        elif choice == "4":
            queue.Display()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
