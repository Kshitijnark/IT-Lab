# write a program for all occarance of vowels present in given string
#class of bill i/p from user current and previous reading: 150+ 
import random
def isoccur(string):
    list=[]
    length=len(string)
    for i in range(length):
            if string[i]=='a' or string[i]=='e' or string[i]=='i' or string[i]=='o' or string[i]=='u' :
                list.append(string[i])
            elif string[i]=='A' or string[i]=='E' or string[i]=='I' or string[i]=='O' or string[i]=='U' :
                list.append(string[i])
            else :
                continue
    return list
def generate_string(length):
    s=[]
    for i in range(length):
        point=random.randint(97,122)
        s.append(chr(point))
    str1 = ""
    for ele in s:
        str1 += ele
    return str1
string=int(input("Enter the String length: "))
a=generate_string(string)
print(a)
print("List: ",isoccur(a))


