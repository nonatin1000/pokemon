import requests
from rest_framework.response import Response


class Pokemon(object):
    BASE_URL = "https://pokeapi.co/api/v2/"

    def __init__(self):
        self.api_url = self.BASE_URL

    def __process_response(self, response):
        response.data = response.json()
        if response.data.get("error"):
            error = response.data.get("error")
            response.reason = f"{error.get('message')}"
            if error.get("reasons"):
                response.reason += f" {error.get('reasons')}"

            if error.get("status_code"):
                response.status_code = error.get("status_code")

        response.raise_for_status()
        return response

    def _get(self, url, querystring=None):
        if querystring:
            response = requests.get(url, params=querystring)
        else:
            response = requests.get(url)
        response = self.__process_response(response)
        return response

    def _post(self, url, data):
        response = requests.post(url, json=data)
        response = self.__process_response(response)
        return response

    def _put(self, url, data):
        response = requests.put(url, json=data)
        response = self.__process_response(response)
        return response

    def list(self, params):
        url = f'{self.api_url}{params}'
        return self._get(url)

    def details(self, id):
        url = f'{self.api_url}evolution-chain/{id}/'
        print("url", url)
        return self._get(url)

    def pokemon_name(self, name):
        url = f'{self.api_url}pokemon/{name}/'
        return self._get(url)
