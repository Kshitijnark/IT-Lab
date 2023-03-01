class bill:
    def __init__(self, prev ,curr):
        self.prev = prev
        self.curr = curr
    def cal_bill(self):
        reading=self.curr-self.prev
        rate=1
        total=0
        if reading<=100:
            rate=5
            total=150+reading*rate
        elif reading<=200:
            rate=10
            total=150+(reading-100)*10+100*5
        elif reading>200:
            rate=15
            total=150+(reading-200)*15+100*5+100*10
        
        print("Unit consumed month: ",reading," units")
        print("your Bill: ₹",total)
print("----------------------------------------------------------------------")
print("                            MahaDisCom                                ")
print("----------------------------------------------------------------------")
prev=int(input("Enter Previous Reading: "))
curr=int(input("Enter Current Reading: "))
b1=bill(prev,curr)
b1.cal_bill()
        