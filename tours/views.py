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
        return render(
            request, 'tours/index.html'
        )


class DepartureView(View):
    def get(self, request, departure):
        return render(
            request, 'tours/departure.html', context={
                'departure': departure,
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
