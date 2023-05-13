from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.


def review(request):
    if request.method == 'POST':
        entered_username = request.POST
        print(entered_username)
        return HttpResponseRedirect("/thank-you")
    return render(request, "reviews/review.html")


def thankyou(request):
    return render(request, "reviews/thankyou.html")
