from random import randint

from django.core.cache import cache
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.decorators.cache import cache_page


# @cache_page(15)
from django.views.generic import ListView

from tools.web.models import Profile


def index(request):
    Profile.objects.create(
        name='Nikoleta Zlateva',
        email='nikoleta@software.it',
    )

    profiles = Profile.objects.all()
    if not cache.get('value2'):
        cache.set('value2', randint(1, 1024), 15)

    count = request.session.get('count') or 0
    request.session['count'] = count + 1

    paginator = Paginator(profiles, per_page=5)
    current_page = request.GET.get('page', 1)

    context = {
        'value': randint(1, 1024),
        'value2': cache.get('value2'),
        'count': request.session.get('count'),
        'profiles': profiles,
        'profiles_page': paginator.get_page(current_page),
    }

    return render(request, 'index.html', context)


class ProfilesListView(ListView):
    model = Profile
    template_name = 'profiles-list.html'
    paginate_by = 5
    #
    # def get_paginate_by(self, queryset):
    #     return self.request.GET.get('pages_count', 1)


def book_details(request, pk):
    last_viewed = request.session.get('last_viewed_books', [])
    last_viewed.append(pk)


