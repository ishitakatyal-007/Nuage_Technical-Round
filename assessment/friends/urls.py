from django.urls import path

app = "friends"

#Create your urls here
from .views import FriendsView, TransactionIOUView

urlpatterns = [
    path("add/", FriendsView.as_view()),
    path("iou/", TransactionIOUView.as_view()),
]