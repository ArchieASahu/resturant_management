def itemslist():
    import random
    print("<"*80)
    print(" "*27," !! ITEMS PAGE !! ")
    print(">"*80)
    fp=open("items.txt")
    c=fp.read()
    cp=fp.readlines()
    print(c)
    fp.close()
    total=0
    l=[]
    l1=[]
    l2=[]
    fp=open("items.txt",'r')
    cp=fp.readlines()
    print("ORDER YOUR  ")
    while True:
        d=input("\nChoose dish number: ")
        l.append(d)
        q=int(input("\nEnter Quantity: "))
        l1.append(q)
        for i in cp:
            k=i.rstrip().split(",")
            if k[0]==d:
                total = total + (q *int(k[2]))
        ch=input("Press 'y' to choose another dish: ").lower()
        if ch=='y':
            continue
        else:
            on=random.randint(1,500) + random.randint(500,1000)
            print("'"*80)
            print("\n ***YOUR ORDER LIST***")
            print(f"\n Order number : {on}")
            l2.append(f"{on},")
            for i in cp:
                k=i.rstrip().split(",")
                for j in range(len(l)):
                    if k[0]==l[j]:
                        print(f"{k[1]},{l1[j]}")
                        l2.append(f"{k[1]},{l1[j]},")
            l2.append("\n")
            print(" TOTAL AMOUNT IS :",total)
            break
    ch1=input("ARE YOU CONFIRM: (Y/N): ")
    if ch1=='Y' or ch1=='y':
        print("\n ---!! Order recieved !!---  ")
        print("\n---Thank yoU---")
        ol=open("orderlist.txt",'a')
        ol.writelines(l2)
        ol.close()
    else:
        print("\n---THANK YOU---")
