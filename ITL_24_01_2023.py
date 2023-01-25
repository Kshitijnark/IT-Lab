# Define a class student which must have properties like id, name, age, marks for maths, 
# science, English, total, percentage, status, grade . Make two function one for inputting
# data 
# id , name, age, maths, science, english
# another function for doing calculation
# total, percentage, status and grade .Status will be passed if the student gets more than 50 
# marks in every subject
# Grade will be 
# a if percentage >=75
# b if percentage >=60 and <75
# c if percentage >=50 and <60
# otherwise no grade
class result :
    def __init__(self, name,id,age):
        self.name = name
        self.age = age
        self.id=id
    def get_data(self):
        
        print("\nEnter The Marks : ")
        print("----------------------------------------------")
        Science=int(input("Enter Science Marks: "))
        Maths=int(input("Enter Maths Marks: "))
        English=int(input("Enter English Marks: "))
        print("----------------------------------------------")
        total_get=Science+Maths+English
        Percentage=int(total_get/3)
        print("Percentage -> ",Percentage,"%")
        if Science>50 and Maths>50 and English>50 :
            print("Status: Passed")
            if(Percentage>=75):
                print("Grade -> A")
            elif(Percentage>=60&Percentage<75):
                print("Grade -> B")
            elif(Percentage>=50&Percentage<60):
                print("Grade -> C")
        else:
            print("Failed\nGrade ->No Grade")
Number=int(input("Total Number of student:"))
for i in range(Number):
    
    print("\nStudent No.",i+1)
    print("----------------------------------------------")
    name1=str(input("Enter Your Name:"))
    id1=int(input("Enter ID:"))
    age1=int(input("Enter age: "))
    print("----------------------------------------------")
    student=result(name1,id1,age1)
    student.get_data()

            

        



