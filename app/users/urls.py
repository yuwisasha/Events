from django.urls import path

from .api import CreateUserView


urlpatterns = [
    path('create_user/', CreateUserView.as_view()),
]