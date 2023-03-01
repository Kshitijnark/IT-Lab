num1=int(input("Order of Matrix num*num: "))
num=num1*num1
a=1
for i in range (1,num1+1):
    for j in range(1,num1+1):
        print(a,end="\t")
        a=a+1
    print()