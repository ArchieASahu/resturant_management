import items
def dupname(name):
    fp=open("customer.txt",'r')
    c=fp.readlines()
    fp.close()
    for i in c:
        i=i.rstrip().split(',')
        if i[0]==name:
            return True
        else:
            return False
def isvalid(pwd):
    d=0
    u=0
    l=0
    s=0
    if len(pwd)>=6:
        for i in pwd:
            if i.isdigit():
                d+=1
            elif i.islower():
                l+=1
            elif i.isupper():
                u+=1
            elif i=='@'or i=='$' or i=='#'or i=='&':
                s+=1
        if d>=1 and l>=1 and u>=1 and s>=1:
            return 'valid'
        else:
            return 'invalid'
def Enamepwd(name,pwd):
    fp=open("customer.txt",'r')
    c=fp.readlines()
    fp.close()
    for i in c:
        i=i.rstrip().split(',')
        if i[0]==name and i[1]==pwd:
            return True
        else:
            return False
def login1():
    name=input("Name : ")
    pwd=input("Create password of 6 characters with one digit,lower_case,upper_case and special character\n password: ")
    name1=dupname(name)
    res=isvalid(pwd)
    while True:
        if name1!=True and res=='valid':
            details=name+','+pwd+'\n'
            fp=open("customer.txt",'a')
            fp.write(details)
            fp.close()
            print("Account created successfully")
            items.itemslist()
            break
        elif name1!=True:
            print("Duplicate name")
            break
        elif res=='invalid':
            print("Invalid password")
            break
        else:
            pass
def login():
    print("="*60)
    print(".................Customer page.................")
    while True:
        print("Select choice\n1. New user\n2. Existing user")
        ch=int(input("Enter your choice : "))
        if ch==1:
            login1()
            break
        elif ch==2:
            name=input("Name : ")
            pwd=input("Enter password : ")
            name_pwd=Enamepwd(name,pwd)
            if name_pwd==True:
                items.itemslist()
                break
            else:
                print("Create an account")
        else:
            break

