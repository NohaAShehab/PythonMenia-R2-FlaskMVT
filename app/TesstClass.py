class Person:
    def __init__(self) -> None:
        self.name = 'Ahmed'
        self.email ='ahmed@gmail.com'



        
p = Person()
for k in p.__dict__:
    print(k)