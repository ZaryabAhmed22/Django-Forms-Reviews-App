from django.urls import path
from . import views
urlpatterns = [
    path("", views.review),
    path("complain/", views.complain),
    path("thank-you/", views.thankyou)
]
