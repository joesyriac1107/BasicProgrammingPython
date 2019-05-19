class Kettle(object):

    def __init__(self,make,price):
        self.make=make
        self.price=price
        self.on = False

kenwood = Kettle("Kenwood",8.9)
print(kenwood.make)
print(kenwood.price)

kenwood.price=12.75
print(kenwood.price)

hamilton =Kettle("Hamilton",9)
print(hamilton.make)
print(hamilton.price)

print("Models: {} = {},{} = {}".format(kenwood.make,kenwood.price,hamilton.make,hamilton.price))


hamilton.eat=4

print(hamilton.eat)