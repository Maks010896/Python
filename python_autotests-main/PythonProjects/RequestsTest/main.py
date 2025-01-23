import requests

URL = 'https://api.pokemonbattle.me'
header = {'Content-Type': 'application/json'}
HEADER = {'trainer_token': 'b2ba0d71c3c6e53b154fb37cb1273b0c'}

body = {
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}

response = requests.post(url=f'{URL}/v2/pokemons', json=body, headers=HEADER)
print(f'Статус код: {response.status_code}. Сообщение: {response.text}') 



body = {
    "pokemon_id": "20833",
    "name": "Ololo"
}

response = requests.patch(url=f'{URL}/v2/pokemons', json=body, headers=HEADER)
print(f'Статус код: {response.status_code}. Сообщение: {response.text}')


body = {
    "pokemon_id": "20833"
}

response = requests.post(url=f'{URL}/v2/trainers/add_pokeball', json=body, headers=HEADER)
print(f'Статус код: {response.status_code}. Сообщение: {response.text}')