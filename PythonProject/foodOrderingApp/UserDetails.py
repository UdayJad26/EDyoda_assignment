from FoodDetails import Food

class User:
    
    def __init__(self) -> None:
        self.users=[{"name":"Uday Jad","phone_number":"9096321350","email_ID":"jaduday@gmail.com","address":"Kodoli","password":"Uday@96","oder_history":[]}]

    def check_userID(self,emailId):
        flag=0
        for u in self.users:
            if u["email_ID"] == emailId: 
                flag=1
                return True
        if flag ==0:
            return False  

    def create_account(self,name,phone_number,email_ID,address,password):
        check=User.check_userID(self,email_ID)
        if check==False:
            self.users.append({"name":name,"phone_number":phone_number,"email_ID":email_ID,"address":address,"password":password,"oder_history":[]})
        else:
            print("EmailID already exist!")
    

    def login(self,emailId,password):
        for u in self.users:
            if u["email_ID"] == emailId and u["password"] == password : return True
            else: False 
    
    def update_profile(self,ID,dict_update):
        count=0
        for u in self.users:
            count +=1
            if u["email_ID"] == ID:
                self.users[count-1].update(dict_update)
    
    def view_prifile(self,ID) :
        for u in self.users:
            if u["email_ID"] == ID :
                print(f"Name: {u.get('name')}")
                print(f"Phone number: {u.get('phone_number')}")
                print(f"Email: {u.get('email_ID')}")     
                print(f"Address: {u.get('address')}")     

    def show_food(self):
        count=0
        for f in Food.foods:
            count +=1
            print(count, end=" ")
            print(f"{f.get('name')} ({f.get('quantity')}) [INR {f.get('quantity')}]")
        
    def order_history(self,ID):
        count=0
        for u in self.users:
            if u["email_ID"] == ID :
                l=self.users[count]["oder_history"]
                if len(l)>0:
                    k=0
                    for i in l:
                        k +=1
                        print(k,end=" ")
                        print(i)
                else:
                    print("You don not have any order history")
            

    def place_order(self,ID,order_list):
        F=Food.foods
        print("\nSelected Oders")
        order=[]
        update_stock_list=[]
        for i in order_list:
            i=int(i)
            print(i, end=" ")
            if F[i-1].get('stock')==0:
                print(F"\n{F[i-1].get('name')} not in stock please order other foods\n") 
            else:
                str1=f"{F[i-1].get('name')} ({F[i-1].get('quantity')}) [INR {F[i-1].get('price')}]"
                order.append(str1)
                stock=F[i-1].get('stock')
                update_stock_list.append([i-1,stock-1])
                print(str1)
        print()
        if len(order) !=0:
            place=str(input("Type 'Y' press enter to place order and 'N' press enter to cancel : "))
        if place=="Y" or place=='y':
            count=0
            for s in update_stock_list:
                F[s[0]].update({"stock":s[1]})
           
            for u in self.users:
                if u["email_ID"] == ID :
                    self.users[count]["oder_history"].extend(order)
            return True
        return False


        
