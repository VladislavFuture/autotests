import requests
import pytest

def test_status_code():
    responses=requests.get('https://api.pokemonbattle.me:9104/trainers',params={'trainer_id':2528})
    assert responses.status_code==200

def test_body():
    responses=requests.put('https://api.pokemonbattle.me:9104/trainers',headers={'trainer_token':'24d0d262fb05b919459cc6e08ac75cbb'},
                                                                                 json={
    "name": "Ash",
    "city": "Tokyo"}) 
    assert responses.json()['message']== "Информация о тренере обновлена"
