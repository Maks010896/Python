import requests
import pytest

URL = 'https://api.pokemonbattle.me'
header = {'Content-Type': 'application/json'}

def test_status_code():
    response = requests.get(url=f'{URL}/v2/trainers')
    assert response.status_code == 200


def test_trainer_name():
    response = requests.get(url=f'{URL}/v2/trainers', params={'trainer_id': 18139})
    assert response.json()['data'][0]["trainer_name"] =='Maga21russia'