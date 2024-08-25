class User:
    def __init__(self, user_id,username):
        self.user_id = user_id
        self.username =username
        self.followers=0
        self.following=0
        self.name = ""
        self.age = 0
        self.email = ""
        self.password = ""
        self.is_admin = False
        self.is_active =False
        self.is_superuser =False
        self.is_staff =False

    def follow(self,user):
        self.following+=1
        user.followers+=1
    def set_name(self,name):
        self.name =name
        return self
    def set_age(self,age):
        self.age = age
        return self
    def set_email(self,email):
        self.email = email
        return self

user_1=User("shayan")
user_2=User("reyhane")
# user_1.set_name("John").set_age(18).set_email("<EMAIL>")
print(user_1.name)
user_1.follow(user_2)