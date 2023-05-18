from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm, ComplainForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView
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


def complain(request):
    if request.method == "POST":
        form = ComplainForm(request.POST)

        if form.is_valid():
            form.save()  # saving data in a model form
            print(form.cleaned_data)
            return HttpResponseRedirect("/thank-you")
    else:
        form = ComplainForm()
    return render(request, "reviews/complain.html", {"form": form})


def thankyou(request):
    return render(request, "reviews/thankyou.html")

# >> CLASS BASED VIEWS


class ThankyouView(View):  # >> Simple Class Based View for Thankyou page
    def get(self, request):
        return render(request, "reviews/thankyou.html")

# >> TemplateView || This is used when the main purpose of a view is to render a template


class ThanyouTemplateView(TemplateView):
    # this is a built in variable name "template_name"
    template_name = 'reviews/thankyou.html'

    # To pass any kind of context data we use get_context_data function
    def get_context_data(self, **kwargs):

        # Callind the super method os that the built in get_context_data is called with the passed data, this code creates a new empty context dictionary
        context = super().get_context_data(**kwargs)

        # Adding new key/value to the context dict
        context["message"] = "Your review has been successfully been submitted"

        # Returning the context dict
        return context


class ReviewsListTemplateView(TemplateView):
    template_name = "reviews/review_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        reviews = Review.objects.all()

        context["reviews"] = reviews

        return context

# >> ListView


class ReviewListListView(ListView):
    template_name = "reviews/review_list.html"

    model = Review

    context_object_name = "reviews"

    def get_queryset(self):
        # Setting up the base query on which we can use all the model querying methods
        base_query = super().get_queryset()

        # filtering reviews
        data = base_query.filter(rating=4)
        print(data)

        return data


class ReviewDetailView(TemplateView):
    template_name = "reviews/review_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        review_id = kwargs["id"]

        selected_review = Review.objects.get(pk=review_id)

        context["review"] = selected_review

        return context
