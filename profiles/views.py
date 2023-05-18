from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect

# Create your views here.


class CreateProfileView(View):
    def get(self, request):
        return render(request, "profiles/create_profile.html")

    def post(self, request):
        # Since request.POST only contains none file data of a form, the data containing any kinf of files can be accesses using request.FILES["name_of_input"]
        print(request.FILES["image"])
        return HttpResponseRedirect("/profiles")
