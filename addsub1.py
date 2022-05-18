class add_sub:
    def __init__(self):
       print("You are going to use arithmetic oprations")
    # define 'add' method
    def add(self, num1, num2):
        self.n1=num1
        self.n2=num2
        return self.n1 + self.n2
    # define 'subtract' method
    def subtract(self, num1, num2):
        self.n1 = num1
        self.n2 = num2
        return self.n1 - self.n2
if __name__ == '__main__':
    x = 10
    y = 6
    # create an instance
    opp = add_sub()
    # call add method
    print(f'{x} + {y} = {opp.add(x, y)}')
    #print(opp.add())
    # call subtract method
    print(f'{x} - {y} = {opp.subtract(x, y)}')
