from django.urls import path


from . import views

urlpatterns = [
    path("", views.CreateProfileCreateView.as_view()),
    path("list", views.ProfilesView.as_view(), name="image-list")
]
