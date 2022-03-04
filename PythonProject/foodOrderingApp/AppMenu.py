
import email

from pyrsistent import discard
from FoodDetails import Food
from UserDetails import User
from AdminDetails import Admin
import re

F=Food()
U=User()
A=Admin()

USER_INPUT='''
Please enter 
1. Admin login 
2. user login
3. Register As A user
99. Quit

'''


def Admin_fuction():
    USER_INPUT='''
    Please enter 
    1. Create Food
    2. View Food list
    3. Edit Food details 
    4. Delete Food
    99. Quit

    '''
    try:
        choice=int(input(USER_INPUT))
    except : 
        choice=-1
    while choice !=99:
        if choice==1:
            print('''To create food please enter FoodName, Quntity, Price, Discount and Stock
                        eg
                          FoodName: Pizza
                          Quntity: 2 pieces or 50 gm or 0.5 kg etc
                          Price : 100 or 110.5
                          Dicscont : 5
                          stock : 15
                          
                          ''')
            try:
                flag=0
                name=str(input("FoodName : "))
                Quntity=str(input("Quntity : "))
                Price=float(input("Price : "))
                Discount=int(input("Discount : "))
                Stock=int(input("Stock : "))
                print()
                if len(name)==0 or len(Quntity)==0:
                    flag=1
                    print("Food name or quantity can be blank")
                if Price<=0 :
                    flag=1
                    print("Price can not be less than or equal to zero")
                if Discount<0 or Stock<0:
                    flag=1
                    print("Discount or Stock can not be less than zero")
                if flag==0:
                    print(F.create_food(name,Quntity,Price,Discount,Stock))
                else:
                    print("\nPlese re-enter your inputs\n")
                    continue
            except:
                print("Somethine went wrong, note price or stock or discont must be in only in numbers eg. 10 or 10.5")
                continue
        elif choice==2:F.view_food()
        elif choice==3:
            ID=str(input("Please enter Food ID : "))
            
            USER_INPUT3='''
                        Please enter 
                        1. To edit food name
                        2. To edit food quntity
                        3. To edit food price
                        4. To edit discount
                        5. Tp edit food stock
                        99. To main menu 
                '''
            try:
                choice3=int(input(USER_INPUT3))
            except:
                choice3=-1
            while choice3 !=99:
                if choice3==1:
                    n=str(input("Please enter updated food name : "))
                    if n!=0:
                        F.edit_food(ID,{"name":n})
                    else:
                        print("/nFood Name can not be blank")
                        continue

                elif choice3==2:
                    q=str(input("Please enter updated food quantity : "))
                    if q!=0:
                        F.edit_food(ID,{"quantity":q})
                    else:
                        print("/nFood quntity can not be blank : ")
                        continue
                elif choice3==3:
                    p=str(input("Please enter updated food price : "))
                    if len(p) >0:
                        F.edit_food(ID,{"price":p})
                    else:
                        print("/nFood price can not be blank")
                        continue

                elif choice3==4:
                    try:
                        d=int(input("Please enter updated discount : "))
                        if d<0:1/0
                        F.edit_food(ID,{"discount":d})
                    
                    except:
                        print("Dicount must be in positive numbers plese retry")
                        continue

                elif choice3==5:
                    try:
                        s=int(input("Please enter updated stock : "))
                        if s<0:1/0
                        F.edit_food(ID,{"stock":s})
                    except:
                        print("Stock must be in positive numbers plese retry")
                        continue

                else: print("Wrong Input please retry")

                try:
                    choice3=int(input(USER_INPUT3))
                except:
                    choice3=-1

        elif choice==4:
            ID=str(input("Please enter Food ID : "))
            F.remove_food(ID)

        else:
            print("Wrong Input, Please retry")
            
        try:
            choice=int(input(USER_INPUT))
        except : 
            print("Wrong password please retry")
            continue

def User_funtion(ID):
    USER_INPUT='''
        Please enter
        1.Place New Order
        2.Order History
        3.Update Profile
        4.View profile
        99. Back main menu

    '''
    try:
        choice=int(input(USER_INPUT))
    except : 
        choice=-1
    

    while choice !=99:
        if choice==1:
            U.show_food()
            order=str(input("Enter Number to place order, If you want to order more than one then enter numbers separated comma eg. 2,3 : "))
            if len(order)==1:
                try:
                    single_order=int(order)
                    r=U.place_order(ID,[single_order])
                    if r==True : print("Order Placed")
                    elif r==False :print("Order cancelled")
                except:
                    print("Wrong input")
                    continue
            elif len(order)>2:
                try:
                    mul_order=order.split(",")
                    r=U.place_order(ID,mul_order)
                    if r==True : print("Order Placed")
                    elif r==False :print("Order cancelled")
                except:
                    print("Wrong input")
                    continue

        elif choice==2:
            U.order_history(ID)
        elif choice==3:
            USER_INPUT2='''
            1.To update Name
            2.To update Phone number
            3.To update EmailID
            4.To update address
            5.To Update Password
            99. Back to main menu

            '''
            try:
                choice2=int(input(USER_INPUT2))
            except : 
                choice2=-1
       
            
            while choice2 !=99:
                if choice2 ==1:
                    n=str(input("Name: "))
                    U.update_profile(ID,{"name":n})
                elif choice2 ==2:
                    pn=str(input("Phone Number: "))
                    U.update_profile(ID,{"phone_number":pn})

                elif choice2 ==3:
                    E=str(input("EmailID: "))
                    U.update_profile(ID,{"email_ID":E})
                elif choice2 ==4:
                    a=str(input("Address: "))
                    U.update_profile(ID,{"address":a})
                elif choice2 ==5:
                    P=str(input("Password: "))
                    U.update_profile(ID,{"password":P})
                else :
                    print("Wrong Input, Please Retry")

                try:
                    choice2=int(input(USER_INPUT2))
                except : 
                    print("Wrong password please retry")
                    continue

        elif choice==4:
            U.view_prifile(ID)        
        
        else:
            print("Wrong Input Plese retry")

        try:
            choice=int(input(USER_INPUT))
        except : 
            print("Wrong password please retry")
            continue

    
    
    
try:
    choice=int(input(USER_INPUT))
except : 
    choice=-1


while choice !=99:
    if choice==1:
        ID=str(input("Please enter User ID : "))
        check_ID=A.check_adminID(ID)
        if check_ID == False:
            print("Invalid ID please contact your admintration (9096321350)")
        elif check_ID == True:
            password=str(input("Password : "))
            check_pass=A.login(ID,password)
            if check_pass ==True:
                print("Logged in successfully!")
                Admin_fuction()
            else:
                print("Wrong password please retry")
                continue
        

    elif choice==2:
        ID=str(input("Please enter Email ID as User ID : "))
        check_ID=U.check_userID(ID)
        if check_ID == False:
            print("Invalid userID or You don't have user account please press 3 to register as user")
        elif check_ID == True:
            password=str(input("Password : "))
            check_pass=U.login(ID,password)
            if check_pass ==True:
                print("Logged in successfully!")
                User_funtion(ID)
            else:
                print("Wrong password please retry")
    elif choice==3:
        flag=0
        name=str(input("Enter Full Name : "))
        phone_number=str(input("Enter 10 digit Phone Number : "))
        EmailID=str(input("Enter Email ID: "))
        Adress=str(input("Enter Address : "))
        password=str(input("Enter Password : "))
        print()
        if len(name)==0:
            flag=1
            print("Name can not be blank")
        if len(phone_number)==10 and re.search("[0-9]{10}",phone_number):pass
        else:
            flag=1
            print("invalid Phone number")
        if "@" in EmailID and "." in EmailID:
            pass
        else: 
            flag=1
            print("Invalid Email ID")
        if len(Adress)==0:
            flag=1
            print("Address can not be blank")
        if len(password)==0:
            flag=1
            print("Password can not be blank")
        
        if flag==0:
            U.create_account(name,phone_number,EmailID,Adress,password)
        else:
            print("Please recreate user account")
            continue
    else: print("Wrong Input, Please retry")


    
    try:
        choice=int(input(USER_INPUT))
    except : 
        print("Wrong password please retry")
        
    




 