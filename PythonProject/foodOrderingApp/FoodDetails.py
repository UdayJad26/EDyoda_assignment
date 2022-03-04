from itertools import count
import random
import string

class Food:
    foods=[
        { "FoodID":'F001',"name":"Tandoori Chicken","quantity": "4 piece","price":150,"discount":5,"stock":10},
        { "FoodID":'F002',"name":"Vegan Burger","quantity": "1 piece","price":50,"discount":2,"stock":2}
       
        ]

    def __init__(self):
        pass
    
    def create_food(self,name,quantity,price,discount,stock):
        Food_ID=''.join(random.choices(string.ascii_uppercase,k=1))+''.join(random.choices(string.digits,k=3))
        Food.foods.append({ "FoodID":Food_ID,"name":name,"quantity":quantity,"price":price,"discount":discount,"stock":stock})

        return "Created successfully"

    def view_food(self):
        if len(Food.foods)==0:
            print("No foods available. Please contact admin to add foods")
        else:
            for values in Food.foods:
                print("FoodID       : ",values["FoodID"])
                print("Food Name    : ",values["name"])
                print("Quantity     : ",values["quantity"])
                print("Price        :   INR",values["price"])
                print("Discount     : ",values["discount"], " %")
                print("Stock        : ",values["stock"])
                print()
        
    def edit_food(self,ID,update_dict):
        count=0
        flag=0
        for f in Food.foods:
            count +=1
            if f.get("FoodID")==ID:
                flag=1
                Food.foods[count-1].update(update_dict)
        if flag==0:
            print("Invalid Food ID")
        
    def remove_food(self,ID):
        count=0
        flag=0
        for f in Food.foods:
            count +=1
            if f.get("FoodID")==ID:
                flag=1
                del Food.foods[count-1]
        if flag==0:
            print("Invalid Food ID")
                        

                    




