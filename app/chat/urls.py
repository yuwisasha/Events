from django.urls import path
from .api import CreateRetrieveConversationView, ListConversationsView

urlpatterns = [
    path("start/", CreateRetrieveConversationView.as_view()),
    path("<int:convo_id>/", CreateRetrieveConversationView.as_view()),
    path("", ListConversationsView.as_view()),
]
