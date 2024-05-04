import items


def owner():
    while True:
        
        print("\twhat do you want to do")
        print("\t1.View the item list")
        print("\t2.Update item in list")
        print("\t3.Dispatch order")
        print("\t4.close")
        ch=input("\nEnter choice\n")
        if ch=='1':
                print(""*20," !! ITEMS PAGE !!",""*20)
                fp=open("items.txt")
                c=fp.read()
                print(c)   
        elif ch=='2':
                l=[]
                fp=open("items.txt",'r')
                cp=fp.readlines()
                for i in cp:
                    k=i.rstrip().split(",")
                    l.append(k[0])
                print(" 1--> Add new item ")
                print(" 2--> Delete an item ")
                print(" 3--> Update the price of an item ")
                ch1= input("\nEnter choice : ")
                if ch1 == '1':
                    item_no=input('Enter item no : ')
                    if item_no in l:
                        print(" Item no is already present !! ")
                    else:
                        item_name=input("Enter item name: ")
                        item_price=input("Enter price of item : ")
                        fp=open("items.txt","a")
                        fp.writelines(item_no + "," + item_name + "," + item_price + "\n")
                        print(" ITEM ADDED SUCCESSFULLY ")
                elif ch1=='2':
                    fp=open("items.txt","r+")
                    c=fp.readlines()
                    fp.seek(0)
                    ch5=input("Enter item no to delete from list : ")
                    if ch5 in l:
                        for i in c:
                            k=i.rstrip().split(",")
                            if k[0]!=ch5:
                                fp.write(i)
                        fp.truncate()
                        print(" Item deleted ")
                    else:
                        print(" Item number not present ")
                        
                elif ch1=='3':
                                
                    fp=open("items.txt",'r')
                    cp=fp.readlines()
                    itemno=input("Enter item no : ")
                    flag=0
                    if itemno in l:
                        name=input("Enter item name: ")
                        price=input("Enter the price to be updated : ")
                        if price.isdigit():
                            for i in range(len(cp)):
                                if name in cp[i]:
                                    cp[i]= itemno + "," + name + "," + price + "\n"

##                                    print(cp[i])
                                    print(" UPDATED SUCCESSFULLY ")
                                    flag=1
                                    break
                            if flag==0:
                                print("NOT FOUND ")
                        else:
                            print(" Price should contain only Digits ")
                        fp=open("items.txt",'w')
                        cp=fp.writelines(cp)
                    else:
                        print(" Item number not present ")
                else:
                    print(" INVALID CHOICE ")
                    break

        elif ch=='3':
                fp=open("orderlist.txt","r")
                c=fp.readlines()
                print(" The list is : ")
                for i in c:
                    print(i)
                fp1=open("orderlist.txt","r+")
                cp=fp1.readlines()
                fp1.seek(0)
                l1=[]
                for i in cp:
                    k1=i.rstrip().split(",")
                    l1.append(k1[0])
                choice=input("Choose item number to dispatch: ")
                if choice in l1:
                    for i in cp:
                        k1=i.rstrip().split(",")
                        if k1[0]!=choice:
                            fp1.write(i)
                    fp1.truncate()
                    print(" Item Dispatched")
                else:
                    print(" Item not Present ")
        elif ch=='4':
                print("***\U0001F60A!! THANK YOU !!\U0001F60A***")
                break
        else:
            print(" INVALID PASSWORD !!")
            print("\n  ---------------****--------------")
