from django.urls import path
from . import views
urlpatterns = [
    path("", views.ReviewView.as_view()),
    path("complain/", views.complain),
    path("thank-you/", views.ThanyouTemplateView.as_view()),
    path("reviews/", views.ReviewListListView.as_view()),
    path("reviews/favourite/", views.AddFavouriteView.as_view()),
    path("reviews/<int:pk>/",
         views.ReviewDetailDetailView.as_view(), name="review-detail")
]
