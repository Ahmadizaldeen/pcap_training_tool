class Storage:

    class_att = []

    def __init__(self, stuff):
        #self.stuff = []
        print(stuff)
        #print(BLUE)
        length = len(self.stuff)
        #print(f'{GREEN}{length}')
        #self.class_att = class_att
        #self.count = class_att.append(length)
    @classmethod
    @type_color_decorator
    def show(cls):
        return cls.class_att
    @type_color_decorator
    def remove(self, prop):
        print("remove")
        #self.stuff.remove(prop)

    @type_color_decorator
    def add(self, prop):
        print("add")
        #self.stuff.append(prop)

    @type_color_decorator
    def get(self,index):
        print("get")
        print(type(self))
        #        print(self.stuff)
        #return self.stuff[index]




# stuff = Storage([10])
# print(type(stuff))
# print(stuff.get(0))
# # stuff.add(5)
# print(stuff.get(0))
#stuff.set("10KG")
#stuff.set("Name")
#print(stuff.count)

#print(stuff.get(0)) #10KG
#print(stuff.art) #['10KG', 'Name']
#print(stuff.get(0))
#stuff.remove(10)
#print(stuff.storage)
# print(stuff.show())
# print(id(stuff.art )== id(stuff.show()))
# stuff.set("Preis")
# print(stuff.show())
# stuff.remove("Preis")
# print(stuff.show())
# print(stuff.count)


class Product:
    def __init__(self):
        self.product = []

    def set_name (self, name):
        self.product.append(name)

    @type_color_decorator
    def get_name (self, index):
        print(index)
        #return self.product[index]

    def set_price(self, price):
        self.price = price
        self.product.append(price)
    @type_color_decorator
    def get_price(self , *args):
        print(type(self))
        #return self.price


auto = Product()
auto.set_name('Auto')
auto.set_price(100)
print(auto)
print(auto.get_price())
print(auto.product)
#print(auto.get_name(1))
print(auto.get_name(int(1)))