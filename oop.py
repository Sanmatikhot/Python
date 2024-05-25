class car :
    def __init__(self,brand,model,year):
      self .brand = brand
      self .model = model
      self .year = year

    def display(self):
        print(self.brand, self.model, self.year)
    def  start(self):
        print("engine  started")
car1 = car("toyota" ,"camry",2020)
car2 = car("honda" ,"civil",2018)

car1.display()
car2.display()

car1.start()
car2.start()




