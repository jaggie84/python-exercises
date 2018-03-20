class Person:
     def __init__(self, name, email, phone):
         self.name = name
         self.email = email
         self.phone = phone
     def greet(self, other_person):
         print('Hello {}, I am {}!'.format(other_person.name, self.name))
sonny = Person('Sonny', 'test@gmail.com', '713-584-3669')
jordan = Person('Jordan', 'test2@gmail.com', '123-456-7890')
sonny.greet(jordan)
jordan.greet(sonny)
print(sonny.name, sonny.email, sonny.phone)
print(jordan.name, jordan.email, jordan.phone)
