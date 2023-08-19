from .views import RoomView
from django.urls import path

urlpatterns=[
    path('room',RoomView.as_view()),
    #RoomView.as_view() is used to convert the RoomView class-based view into a callable view function that can be used in URL patterns

]