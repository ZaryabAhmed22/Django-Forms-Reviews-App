from django.urls import path
from . import views
urlpatterns = [
    path("", views.review),
    path("complain/", views.complain),
    path("thank-you/", views.ThanyouTemplateView.as_view()),
    path("reviews/", views.ReviewListListView.as_view()),
    path("reviews/<int:id>/",
         views.ReviewDetailView.as_view(), name="review-detail")
]
