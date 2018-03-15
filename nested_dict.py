ramit = {
   'name': 'Ramit',
   'email': 'ramit@gmail.com',
   'interests': ['movies', 'tennis'],
   'friends': [
     {
       'name': 'Jasmine',
       'email': 'jasmine@yahoo.com',
       'interests': ['photography', 'tennis']
}, 
{
        'name': 'Jan',
        'email': 'jan@hotmail.com',
        'interests': ['movies', 'tv']
}
]
}

print(ramit.get('email'))
print(ramit.get('friends')[0].get('email'))
print(ramit.get('interests'))
print(ramit.get('friends')[1].get('interests'))
