class Animal: #create the parent class

    alive = True #create the class variable 'alive'.

    #create methods
    def eat(self):
        print("This animal is eating.")

    def sleep(self):
        print("This animal is sleeping.")

class Rabbit(Animal): #pass the name of the parent class Animal to inherit to Rabbit, will have access
                     #to Animal class and eat and sleep defined methods.
    def run(self):
        print("This rabbit is running.")

class Fish(Animal):
    def swim(self):
        print("This fish is swimming.")
class Hawk(Animal):
    def fly(self):
        print("This hawk is flying.")

rabbit = Rabbit() #object
fish = Fish()
hawk = Hawk()

rabbit.run()
fish.swim()
hawk.fly()

print(rabbit.alive)
fish.eat() #calls the eat method and outputs
hawk.sleep() #calls the sleep method and outputs