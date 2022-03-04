
class Admin:

    def __init__(self) -> None:
        self.admins=[{"ID":"admin01","phone_number":"9096321350","email_ID":"jaduday@gmail.com","password":"qwerty@2022"},
        {"ID":"admin02","phone_number":"8149679530","email_ID":"abcdd@gmail.com","password":"aabbcc@2022"}]

    def check_adminID(self,Id):
        flag=0
        for u in self.admins:
            if u["ID"] == Id: 
                flag=1
                return True
        if flag ==0:
            return False 


    def login(self,Id,password):
        for u in self.admins:
            if u["ID"] == Id and u["password"] == password : return True
            else: False 