class Dog:
    def __init__(self,name,height,age):
        self.name=name
        self.height=height
        self.age=age
    def display(self):
        print("The name of this dog is: ",self.name)
        print("The height of a male Golden Retriever is: ",self.height)
        print("The age of this dog is around: ",self.age)
class Golden_Retriever(Dog):
    def __init__(self,name,height,age,popularity):
        self.popularity=popularity
        print("The popularity of this dog is that: ",self.popularity)
        Dog.__init__(self,name,height,age)
c=Golden_Retriever("Golden Retriever","23-24 inches","10-12years old","They are ranked in the top 5 in the U.S")
c.display()
