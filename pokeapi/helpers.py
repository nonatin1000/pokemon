from pokeapi.pokemon_api import Pokemon

pokemon = Pokemon()


def evolves_to(response):
    evolutions = []
    for evolution in response['results']:
        id = evolution['url'].split('/')[-2]
        resp_detail = pokemon.details(id).json()
        evolutions.append({
            'name': resp_detail['chain']['species']['name'],
            'evolves_to': resp_detail['chain']['evolves_to'][0]['evolution_details'],
        })

    return evolutions


def evolves_to_detail(response):
    return {
        'name': response['chain']['species']['name'],
        'evolves_to': response['chain']['evolves_to'][0]['evolution_details'],
    }
