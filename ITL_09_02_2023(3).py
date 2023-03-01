num=int(input("Enter the Order of Matrix: "))
#input for 1st Matrix
print("Input to 1st Matrix: ")
matrix1=[]
for i in range(num):
    a=[]
    matrix1.append(a)
    print("Enter Rowwise: ")
    for j in range(num):
        element=int(input("Element: "))
        matrix1[i].append(element)
print("Matrix 1:\n")
for i in range(num):
    for j in range(num):
        print(matrix1[i][j],end="\t")
    print()

#input for 2nd matrix
print("Input to 2nd Matrix: ")
matrix2=[]
for i in range(num):
    a=[]
    matrix2.append(a)
    print("Enter Rowwise: ")
    for j in range(num):
        element=int(input("Element: "))
        matrix2[i].append(element)
print("Matrix 2:\n")
for i in range(num):
    for j in range(num):
        print(matrix2[i][j],end="\t")
    print()
#output

matrix3=[]
for i in range(num):
    a=[]
    matrix3.append(a)
    print("Enter Rowwise: ")
    for j in range(num):
        element=matrix1[i][j]*matrix2[i][j]
        matrix3[i].append(element)
print("Output:\n")
for i in range(num):
    for j in range(num):
        print(matrix3[i][j],end="\t")
    print()