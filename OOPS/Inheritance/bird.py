# Create a Bird class with a method fly(). Create two subclasses, Parrot and Penguin, 
# where the Parrot class has fly() display "can fly" and the Penguin class overrides it
#  to display "cannot fly."

class Bird:
    def fly(self):
        pass


class Parrot(Bird):
    def fly(self):
        print("Can fly")

class Penguin(Bird):
    def fly(self):
        print("Cannot fly")

parrot = Parrot()
parrot.fly()

penguin = Penguin()
penguin.fly()
