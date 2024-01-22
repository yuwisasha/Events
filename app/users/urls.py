from django.urls import path

from .api import CreateUserView, ListUserView


urlpatterns = [
    path("sign_up/", CreateUserView.as_view()),
    path("user_list/", ListUserView.as_view()),
]
