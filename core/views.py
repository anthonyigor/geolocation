from django.shortcuts import render
from django.views.generic import View
from utils import yelp_search, get_client_data


class IndexView(View):

    def get(self, request, *args, **kwargs):
        items = []
        city = None

        # loop até encontrar a cidade referente ao IP do usuário
        while not city:
            ret = get_client_data()
            city = ret['city']

        # recebe a palavra-chave da busca informada, e a localização (caso o usuário queira informar outra)
        query = request.GET.get('key', None)
        loc = request.GET.get('loc', None)

        location = city
        context = {
            'city': city,
            'busca': False,
        }

        if loc:
            location = loc

        # se uma pesquisa for feita pelo usuário, é realizada uma busca na API e os dados são armazenados no context
        if query:
            items = yelp_search(keyword=query, location=location)
            context = {
                'items': items,
                'city': location,
                'busca': True
            }
        return render(request, 'index.html', context)
