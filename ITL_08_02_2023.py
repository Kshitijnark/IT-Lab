list=[[2,89,78,59],[1,9],[8,5,7],[6,25,4]]

final = []

for i in list:
    for j in i:
         final.append(j)
final.sort()

print("Sorted List\n",final)