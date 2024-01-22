from django.urls import path

from .api import CreateEventView, RetrieveEventView, ListEventView


urlpatterns = [
    path("create_event/", CreateEventView.as_view()),
    path("<int:pk>/", RetrieveEventView.as_view()),
    path("", ListEventView.as_view()),
]
