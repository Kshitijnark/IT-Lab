#25/01/2023
#Stack
class Stack:
    def __init__(self,stack):
        self.stack=[]
    def push(self,data):
        self.stack.append(data)
    def pop(self):
        if(len(self.stack)==0):
            print("Stack is Empty....\n")
        else:
            self.stack.pop()
    def display(self):
        print(self.stack)
    def peek(self):
        top=self.stack[-1]
        print(top)
s1=Stack([])
while(True):
    print("------------------------------------------")
    print("Enter the choice:\n1. Push\n2. Pop\n3. Display\n4. Peek\n5. Exit")
    print("------------------------------------------")
    ch=int(input("Choice: "))
    if(ch==1):
        num=int(input("Enter the Number: "))
        s1.push(num)
        s1.display()
    if(ch==2):
        print("Element Popped: ",s1.peek())
        s1.pop()
        s1.display()
    if(ch==3):
        print("Displaying Stack: ")
        s1.display()
    if(ch==4):
        print("Topmost Element:",s1.peek())
    if(ch==5):
        break





