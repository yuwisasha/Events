from django.urls import path

from .api import CreateOrganizationView


urlpatterns = [
    path('create_organization/', CreateOrganizationView.as_view()),
]
