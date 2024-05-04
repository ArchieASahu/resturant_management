print(" "*30,end="")
print(".........Welcome to our Restaurant..........")
print("Select choice\n1. Customer\n2. Restaurant Owner")
ch=int(input("enter your choice 1 or 2 : "))
import user
import owner
if ch==1:
    user.login()
elif ch==2:
    pwd=input("Password:")
    if pwd=='Dom@123':
        print("------Logged in successfully------")
        owner.owner()
    else:
        print("password is wrong")
else:
    print("Invalid choice")
