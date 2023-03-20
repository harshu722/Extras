class Geetha:
    def __init__(self,x):
        self.x = x

    def __add__(self,other):
        return Geetha(self.x + other.x)

arya = Geetha(1)
ajay = Geetha(2)
subbi = arya + ajay
print(subbi.x)
