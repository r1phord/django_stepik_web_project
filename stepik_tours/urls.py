from django.urls import path

from tours.views import MainView, DepartureView, TourView, custom_handler404, custom_handler500

handler404 = custom_handler404
handler500 = custom_handler500

urlpatterns = [
    path('', MainView.as_view()),
    path('departure/<str:departure>/', DepartureView.as_view()),
    path('tour/<int:id>/', TourView.as_view()),
]
