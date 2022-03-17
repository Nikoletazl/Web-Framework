from random import randint

from django.core.cache import cache
from django.shortcuts import render
from django.views.decorators.cache import cache_page


# @cache_page(15)
def index(request):
    if not cache.get('value2'):
        cache.set('value2', randint(1, 1024), 15)

    count = request.session.get('count') or 0
    request.session['count'] = count + 1

    context = {
        'value': randint(1, 1024),
        'value2': cache.get('value2'),
        'count': request.session.get('count')
    }

    return render(request, 'index.html', context)


def book_details(request, pk):
    last_viewed = request.session.get('last_viewed_books', [])
    last_viewed.append(pk)


