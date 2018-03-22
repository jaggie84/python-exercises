class Vehicle:
     def __init__(self, make, model, year):
         self.make = make
         self.model = model
         self.year = year
     def print_info(self):
         print('Car make: {} //Car Model: {} //Car Production Year: {}.'.format(self.make, self.model, self.year))
car = Vehicle('Nissan', 'Leaf', '2015')
print(car.make, car.model, car.year)
car.print_info()
