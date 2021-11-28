from faker import Faker


fake = Faker()

def user_data(name=None, surname=None):
    if name is None:
        name = fake.first_name()
    if surname is None:
        surname = fake.last_name()
    return {'name':name, 'surname':surname}