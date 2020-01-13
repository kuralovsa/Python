class Human():
    def _init_(self,human):
        self.human="Serik"
class Animal():
    def _init_(self):
        self.dangerous = None
        self.ani= None
    def choose_animal(self,animal):
        self.ani=animal
        if animal=="Dog":
            self.dangerous= False
            print(f"{animal} is dangerous for human :{self.dangerous}")
        if animal=="Spider":
            self.dangerous= True
            print(f"{animal} is dangerous for human :{self.dangerous}")
        if animal=="Lion":
            self.dangerous= True
            print(f"{animal} is dangerous for human:{self.dangerous}")
a=Animal()
a.choose_animal("Dog")
a.choose_animal("Lion")
a.choose_animal("Spider")