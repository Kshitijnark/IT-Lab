class Queue:
    def __init__(self,queue):
        self.queue=[]
    def enqueue(self,data):
        self.queue.append(data)
    def top(self):
        return self.queue[0]
    def dequeue(self):
        if(len(self.queue)==0):
            print("Queue is Empty")
        else:
             self.queue.pop(0)
    def lastmost(self):
        print(self.queue[-1])
    def display(self):
        print(self.queue)
q1=Queue([])
while(True):
    print("------------------------------------------")
    print("Enter the choice:\n1. Enqueue\n2. Dequeue\n3. Display\n4. Topmost\n5. Lastmost\n6. Exit")
    print("------------------------------------------")
    ch=int(input("Choice: "))
    if(ch==1):
        num=int(input("Enter the Number: "))
        q1.enqueue(num)
        q1.display()
    if(ch==2):
        print("Element processed: ",q1.top())
        q1.dequeue()
        q1.display()
    if(ch==3):
        print("Displaying Stack: ")
        q1.display()
    if(ch==4):
        print("Topmost Element:",q1.top())
    if(ch==5):
        print("LastMost Element: ",q1.lastmost())
    if(ch==6):
        break


        