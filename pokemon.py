import requests
import random

print('\n')
print("| _________________________________________|")
print("|                                          |")
print("|      Welcome to the CFG Pokemon Gym      |")
print("|__________________________________________|")
print("")


def random_pokemon():
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()
    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
        'base_experience': pokemon['base_experience'],
        'order': pokemon['order'],
    }

def run():
    pokemon_user = random_pokemon()
    comp_pokemon = random_pokemon()

    print('Your pokemon is {}'.format(pokemon_user['name']))
    print('ID {}'.format(pokemon_user['id']))
    print('Height {}'.format(pokemon_user['height']))
    print('Weight {}'.format(pokemon_user['weight']))
    print('Base experience {}'.format(pokemon_user['base_experience']))
    print('Order {}'.format(pokemon_user['order']))
    print('\n')

    user_choice = input('Which attribute would you like to compare to the computer? id, height, weight, base experience or order ').lower()

    print('Team Rocket drew {}'.format(comp_pokemon['name']))

    if user_choice == 'height':
        if pokemon_user['height'] > comp_pokemon['height']:
            print('You win')
        elif pokemon_user['height'] == comp_pokemon['height']:
                print('It\'s a draw')
        else:
            print('Team Rocket win!')

    elif user_choice == 'id':
        if pokemon_user['id'] > comp_pokemon['id']:
            print('You win')
        elif pokemon_user['id'] == comp_pokemon['id']:
            print('It\'s a draw')
        else:
            print('Team Rocket win!')

    elif user_choice == 'base experience':
        if pokemon_user['base_experience'] > comp_pokemon['base_experience']:
            print('You win')
        elif pokemon_user['base_experience'] == comp_pokemon['base_experience']:
            print('It\'s a draw')
        else:
            print('Team Rocket win!')

    elif user_choice == 'weight':
        if pokemon_user['weight'] > comp_pokemon['weight']:
            print('You win')
        elif pokemon_user['weight'] == comp_pokemon['weight']:
            print('It\'s a draw')
        else:
            print('Team Rocket win!')

    elif user_choice == 'order':
        if pokemon_user['order'] > comp_pokemon['order']:
            print('You win')
        elif pokemon_user['order'] == comp_pokemon['order']:
            print('It\'s a draw')
        else:
            print('Team Rocket win!')

run()
