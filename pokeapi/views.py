from crypt import methods

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.views import Response

from pokeapi.helpers import evolves_to, evolves_to_detail
from pokeapi.pokemon_api import Pokemon

pokemon = Pokemon()


class PokemonViewSet(viewsets.ViewSet):
    # lista 20 pokemons e suas evolucoes
    def list(self, request):
        response = pokemon.list(params='evolution-chain/').json()
        evolutions = evolves_to(response)
        return Response(evolutions)

    # Recebe o nome de um pokemon
    @action(methods=['get'], detail=False, url_path='pokemon_name')
    def pokemon_name(self, request):
        name = self.request.query_params.get('name')
        if not name:
            return Response({"error": "name is required"})
        response = pokemon.pokemon_name(name).json()
        return Response(response)

    # Mostra o nome e a evolucao de um pokemon
    @action(methods=['get'], detail=False, url_path='detail')
    def pokemon_details(self, request):
        id = self.request.query_params.get('id')
        if not id:
            return Response({"error": "id is required"})
        response = pokemon.details(id).json()
        return Response(evolves_to_detail(response))
