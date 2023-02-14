class Person:
    name = ''
    age = ''
    phone = ''
    game = ''

    def __init__(self, nameP, ageP, phoneP,  gameP):
        self.name = nameP
        self.age = ageP
        self.phone = phoneP
        self.game = gameP

    def printID(self):
        print(f"Person Name : {self.name}\nHis Age: {self.age}\nHis Phone: {self.phone}\nhe likes to play: {self.game}")
