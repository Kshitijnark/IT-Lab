answer=int(input("Enter the number of sublists: "))
list=[]
for i in range (answer):
    list1=[]
    list.append(list1)
    num=int(input("Number of Elements for sublist : "))
    print("Input to new sublist: \nEnter Elements: ")
    for j in range(num):
        element=int(input("Element :"))
        list[i].append(element)
print(list)
finallist = sorted(list, key=len)
print(finallist)
