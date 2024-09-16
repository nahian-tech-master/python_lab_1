user = {
    'name': 'my name',
    'age': 28,
    'email': 'myemail@gmail.com',
    'is_verified': True
}

print(user)

print(user['name'])
print(user['age'])

print(user.get('password'))

user['age'] = 29
print(user)

user['job'] = 'teaching'
print(user)
