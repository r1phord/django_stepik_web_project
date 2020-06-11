from django.shortcuts import render
from django.views import View
from django.http import HttpResponseNotFound


def custom_handler404(request, exception):
    return HttpResponseNotFound('Страница не найдена. Ошибка в запросе')


class MainView(View):
    def get(self, request):
        return render(
            request, 'tours/index.html'
        )


class DepartureView(View):
    def get(self, request, departure='anywhere'):
        return render(
            request, 'tours/departure.html', context={
                'departure': departure,
            }
        )


class TourView(View):
    def get(self, request, id=0):
        return render(
            request, 'tours/tour.html', context={
                'id': id,
            }
        )
