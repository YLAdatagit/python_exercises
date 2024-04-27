def greet_user(name):
    print(f"Hello {name.title()}")

greet_user('shi')
greet_user('ye lin aung')
def describe_pet(animal_type , pet_name='Yoyo' ):
    print(f"I have a {animal_type} with the name, {pet_name}.")

describe_pet(pet_name = 'Yoyo', animal_type= 'dog')
describe_pet( animal_type= 'dog', pet_name = 'Yoyo')
describe_pet(   'Yoyo','dog')
describe_pet( 'Yoyo')