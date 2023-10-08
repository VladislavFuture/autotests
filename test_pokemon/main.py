import requests


response_create=requests.post('https://api.pokemonbattle.me:9104/pokemons', json={
    
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
},headers= {"Content-Type":"application/json", "trainer_token" :"24d0d262fb05b919459cc6e08ac75cbb"})
print(response_create.text)

response_change=requests.put('https://api.pokemonbattle.me:9104/pokemons', json={
    
     "pokemon_id": "12132",
    "name": "LINtia",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
},headers= {"Content-Type":"application/json", "trainer_token" :"24d0d262fb05b919459cc6e08ac75cbb"}) 

print(response_change.text)

response_in_pokeball=requests.post('https://api.pokemonbattle.me:9104/trainers/add_pokeball', json={
    
    
    "pokemon_id": "12132"

},headers= {"Content-Type":"application/json", "trainer_token" :"24d0d262fb05b919459cc6e08ac75cbb"}) 

print(response_in_pokeball.text)
