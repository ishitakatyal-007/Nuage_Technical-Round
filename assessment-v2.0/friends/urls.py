from django.urls import path

app = "friends"

#Create your urls here
from .views import CreateUserView, ListUserView, CreateIOUView

urlpatterns = [
    path("add/", CreateUserView.as_view()),
    path("users/", ListUserView.as_view()),
    path("iou/", CreateIOUView.as_view()),
]