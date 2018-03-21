class Vehicle:
     def __init__(self, make, model, year):
         self.make = make
         self.model = model
         self.year = year
     def print_info(self):
         print('My car was made by {}, the model is a {}, and it was produced in {}!'.format(self.make, self.model, self.year))
car = Vehicle('Nissan', 'Leaf', '2015')
print(car.make, car.model, car.year)
car.print_info()
