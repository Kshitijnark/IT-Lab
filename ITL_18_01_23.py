import numpy
R1 = int(input("Enter the number of rows:"))
C1 = int(input("Enter the number of columns:"))

# Initialize matrix
matrix1 = []
print("Enter the entries rowwise:")

# For user input
for i in range(R1):		 
	a =[]
	for j in range(C1):	
		a.append(int(input()))
	matrix1.append(a)
print(matrix1)


# array input 2
matrix2 = []
print("Enter the entries rowwise:")
for i in range(R1):		 
	b =[]
	for j in range(C1):	 
		b.append(int(input()))
	matrix2.append(b)
print(matrix2)
print("\n Matrix 1 is ",matrix1)
print("\n Matrix 2 is ",matrix2)
def add(matrix1,matrix2,R1,C1):
    matrix3 = []
    for m in range(R1):		 
        add_arr=[]
        for n in range (C1):
            add_arr.append(matrix1[m][n]+matrix2[m][n])
        matrix3.append(add_arr)
    print("\nAddition of Two Matrix: ")
    print(numpy.array(matrix3))
def sub(matrix1,matrix2,R1,C1):
    matrix5 = []
    for m in range(R1):		 
        sub_arr=[]
        for n in range (C1):
            sub_arr.append(matrix1[m][n]-matrix2[m][n])
        matrix5.append(sub_arr)
    print("\nSubtraction of Two Matrix: ")
    print(numpy.array(matrix5))
def Check_symmetric(matrix1,R1,C1):
    if R1!=C1:
        print("Matrix is not Square !!!!")
    else:
            matrix4=[]
            for m in range(R1):
                trans_arr=[]
                for n in range(C1):
                    trans_arr.append(matrix1[n][m])
                matrix4.append(trans_arr)
            #print(matrix4)
            print("\nChecking Symmetric or not: ")
            print(matrix4==matrix1)
def isbinary(matrix1,R1,C1):
    print("\nChecking a binary matrix: ")
    count=0
    for m in range(R1):
        for n in range(C1):
            if(matrix1[m][n]!=0 and matrix1[m][n]!=1):
                count=1
                break
            else:
                continue
    if(count==1):print(False)
    else:print(True)
add(matrix1,matrix2,R1,C1)
sub(matrix1,matrix2,R1,C1)
Check_symmetric(matrix1,R1,C1)
isbinary(matrix1,R1,C1)
        


