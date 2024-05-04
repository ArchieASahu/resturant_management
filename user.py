import items
def login():
    print("*"*80)
    print(" "*27," !! LOGIN PAGE !!")
    print(" 1.New User")
    print(" 2.Existing User")
    ch1=input("Enter choice")
    if ch1=='1':
        def newuser():
            fp=open("customer.txt")
            c=fp.readlines()
            name=input("\nEnter your name: ")
            p=input("Enter your Password: ")
            flag=0
            for i in c:
                if name in i:
                    print("\n  USERNAME ALREADY EXISTS !!")
                    flag=1
                    break
                       
            if flag==0:
                di="0123456789"
                ca="QWERTYIOPASDFGHJKLZXCVBNM"
                sa="qwertyuiopasdfghjklzxcvbnm"
                sc="!@#$%^&8?/"
                d,c,s,w,flag=0,0,0,0,0
                if len(p)>=6:
                    for i in p:
                        if i in di:
                            d=d+1
                        elif i in ca:
                            c=c+1
                        elif i in sa:
                            s=s+1
                        elif i in sc:
                            w=w+1
                        else:
                            pass
                    if d>=1 and c>=1 and s>=1 and w>=1:
                        print("\nPASSWORD SUCCESSFULLY ADDED")
                        print("\n"," "*4,"--->"," !! ACCOUNT CREATED !! ","<---")
                        fp=open("customer.txt","a")
                        fp.writelines(name+","+p+"\n")
                        fp.close()
                        items.itemslist()  
                if len(p)>=6:
                    if d==0:
                        print("No digit")
                        flag=1
                    if c==0:
                        print("No uppercase letters")
                        flag=1
                    if s==0:
                        print("No lowercase alphabets")
                        flag=1
                    if w==0:
                        print("No special characters")
                        flag=1
                if len(p)<6:
                    print("Length of password should be more than 6")
                    flag=1
                if flag==1:
                    print("   INVALID PASSWORD  !!")
                    print("Enter valid Password")
                    newuser()
        newuser()

            
    elif ch1=='2':
        def password():
            name=input('\nEnter name: ')
            p=input("Enter Password : ")
            k=(name + "," + p + "\n")
            fp=open("customer.txt")
            c=fp.readlines()
            flag=0
            for i in c:
                if k in i:
                    flag=1
            if flag==1:
                print("\n","--->"," !! LOGIN SUCCESSFULL !! ","<---")
                items.itemslist()
            if flag==0:
                print("\nInvalid Username or Password")
                print("\nPlease enter valid username and password")
                password()
        password()
##            else:
##              print("Invalid")
