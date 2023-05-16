from django.urls import path
from . import views
urlpatterns = [
    path("", views.review),
    path("complain/", views.complain),
    path("thank-you/", views.ThanyouTemplateView.as_view()),
    path("reviews/", views.ReviewsListView.as_view()),
    path("reviews/review-detail/<int:id>/", views.RevieDetailView.as_view())
]
