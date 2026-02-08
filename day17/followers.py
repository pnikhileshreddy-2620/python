class Follows:
    def __init__(self,id,name):
        self.id = id
        self.name = name
        self.followers=0
        self.following =0

    def follow(self,id):
         id.followers +=1
         self.following +=1

u1 =Follows(1,'dell')
u2=Follows(2,'Hp')
print(u1.followers,u1.following)
u2.follow(u1)
print(u1.followers,u1.following)
u1.follow(u2)
print(u2.following,u2.followers)
for i in range(0,5):
    if u1.followers in u2:
        break
    else:
        u2.follow(u1)

print(u1.followers)