class amazon:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def info(self):
        print("This is product and am class is invoked. The name is {self.name} This costs {self.price} rupees.")
class flipkart:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def info(self):
        print(f"This is product and fli class is invoked. The name is {self.name}. T his costs {self.price} rupees.")
FLP = flipkart("Iphone", 2.5)
AMZ = amazon("Iphone", 4)
for product1 in (FLP, AMZ):
    product1.info()
