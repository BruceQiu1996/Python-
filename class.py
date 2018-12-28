class Dog():
    #必须有这么方法
    def __init__(self,name,dog_type):
        self.name=name
        self.dog_type=dog_type

    def print_dog_info(self):
        print(self.name+" is a "+self.dog_type)

my_dog=Dog('瞧瞧','金毛')
my_dog.print_dog_info()
#继承语法
class car():
    def __init__ (self,color,price):
        self.color=color
        self.price=price
    def print_color_and_price(self):
        print(self.color+"$"+self.price)
class electricCar(car):
    def __init__(self,color,price):
        super().__init__(color,price)
        self.battery=10
car=electricCar("蓝色","1000000")
car.print_color_and_price()