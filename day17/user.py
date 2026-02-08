class user:
    """__init__ constructors"""
    def __init__(self,id,name):
        # initial attributes
        self.id =id
        self.name =name
        print("USER CREATED")



# user1 =user()
# user1.id=1
# user1.name ="jack"
# print(user1.name)

user1 =user(1,'jack')
user2 = user(2,'dell')
print(user2.name)
user2.name='dhp'
print(user2.name)