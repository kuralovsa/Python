class Korzina():
    def _init_(self):
        self.capacity = None
        self.object = None

    def choose_obj(self, obj):
        self.object=obj
        if obj =="Paper":
            self.capacity=100
            print(f"capacity for {obj}-{self.capacity}")
        if obj =="Bottle":
            self.capacity=10
            print(f"capacity for {obj}-{self.capacity}")
    def add_obj(self):
        self.capacity-=1
        print(f"space left - {self.capacity}")

class Pocket(Korzina):
    def add_obj(self):
        self.capacity-=10
        print(f"space left - {self.capacity}")

a=Korzina()
a.choose_obj("Paper")
a.add_obj()

a.choose_obj("Bottle")
a.add_obj()
r=Pocket()
r.choose_obj("Paper")
r.add_obj()
r.choose_obj("Bottle")
r.add_obj()