from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import FileForm
from .models import UserProfile
from django.views.generic.edit import CreateView

# Helper functions


def store_file(file):
    # this only works for jpg and is pure python way of storing a file
    with open("temp/image.jpg", "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)

# Create your views here.


class CreateProfileCreateView(CreateView):
    pass


class CreateProfileView(View):
    def get(self, request):
        form = FileForm()
        return render(request, "profiles/create_profile.html", {"form": form})

    def post(self, request):
        submitted_form = FileForm(request.POST, request.FILES)

        if submitted_form.is_valid():
            # store_file(request.FILES["image"])
            # Since request.POST only contains none file data of a form, the data containing any kinf of files can be accesses using request.FILES["name_of_input"]
            print(request.FILES["user_image"])
            profile = UserProfile(image=request.FILES["user_image"])
            profile.save()
            return HttpResponseRedirect("/profiles")

        return render(request, "profiles/create_profile.html", {"form": submitted_form})
