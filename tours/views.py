from random import sample

from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render
from django.views import View

from data import tours, departures


def custom_handler404(request, exception):
    return HttpResponseNotFound('Страница не найдена.')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера.')


class MainView(View):
    def get(self, request):
        random_keys = sample(tours.keys(), 6)
        random_tours = {key: tours.get(key) for key in random_keys}
        return render(
            request, 'tours/index.html', context={
                'tours': random_tours
            }
        )


class DepartureView(View):
    def get(self, request, departure):
        print('=' * 10)
        departure_tours = {key: value for key, value in tours.items() if value['departure'] == departure}
        print('-' * 10)
        return render(
            request, 'tours/departure.html', context={
                'departure': departures.get(departure),
                'tours': departure_tours
            }
        )


class TourView(View):
    def get(self, request, id):
        tour = tours.get(id)
        return render(
            request, 'tours/tour.html', context={
                'id': id,
                'tour': tour,
                'stars': '★' * int(tour['stars']),
                'dep': departures.get(tour['departure'])
            }
        )
