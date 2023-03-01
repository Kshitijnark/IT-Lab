def concat(string1,string2):
    string3=string1+string2
    return string3
def rever(string1):
    str_reverse=string1[::-1]
    return str_reverse
def occurance(string1,letter):
    count = 0
    for i in string1:
        if i == letter:
            count = count + 1
    print(letter," occur in string ",count," times.")
def finding(string1,string2):
    result=string1.find(string2)
    if(result>=0):
     print("Found")
    else:
        print("Not found")
def spilting(string1,index):
    string2=string1[index::]
    return string2
while True :
    print("-----------------------------------")
    print("String Operations:")
    print("1. Concatination")
    print("2. Reverse")
    print("3. Capatalize")
    print("4. Occurance of letter")
    print("5. Length of string")
    print("6. Make Upper Case")
    print("7. Spiliting")
    print("8. Exit")
    print("-----------------------------------")
    ch=int(input("Enter the Choice: "))
    if ch==8:
        break
    match (ch):
        case 1:
            string1=input("Enter String1 :")
            string2=input("Enter String2 :")
            print("Concatinated String: ",concat(string1,string2))
            
        case 2:
            string1=input("Enter String1 :")
            print("Reversed String",rever(string1))
           
        case 3:
            string1=input("Enter String1 :")
            print("Capatalize String: ",string1.capitalize())
            
        case 4:
            string1=input("Enter String1 :")
            string2=input("Enter substring :")
            occurance(string1,string2)
            
        case 5: 
            string1=input("Enter String1 :")
            print("length of string ",len(string1))
        case 6:
            string1=input("Enter String1 :")
            print("Uppercase: ",string1.upper())
        case 7:
            string1=input("Enter String1 :")
            index=int(input("Enter Index: "))
            print("Splited String: ",spilting(string1, index))



            



