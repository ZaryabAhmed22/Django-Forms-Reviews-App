from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
# Create your views here.


def review(request):
    # >> Manually collecting data
    # if request.method == 'POST':
    #     entered_username = request.POST
    #     print(entered_username)
    #     return HttpResponseRedirect("/thank-you")

    # >> Collecting data using Django | in this code we are checking if the request method is post, and if it is post, we are creating a new form using the data entered by the user "request.POST" (is the data), then we will check if the form submission was valid using the bilt in function is_valid, storing the user entred data into the Review model using form.cleaned_data and send a redirect and print the data "form.cleaned_data".
    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = Review(
                user_name=form.cleaned_data['user_name'], review_text=form.cleaned_data['review_text'], rating=form.cleaned_data['rating'])
            review.save()
            print(form.cleaned_data)
            return HttpResponseRedirect("/thank-you")
    else:
        form = ReviewForm()

    return render(request, "reviews/review.html", {"form": form})


def thankyou(request):
    return render(request, "reviews/thankyou.html")
