from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import ReviewForm, ComplainForm
from .models import Review, Complain
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView
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


class ComplainCreateView(CreateView):
    model = Complain

    form_class = ReviewForm

    template_name = "reviews/review.html"

    success_url = "/thank-you"


class ReviewView(FormView):
    # To make use of FormView, we have to do 4 basic steps;
    # i) declare the form class that we have to render
    # ii) Declare the template where we have to render the form
    # iii) Declare the success url where you want to redirect after successful form submission
    # iv) THIS IS ONLY APPLICABLE FOR MODELFORMS >> Declare a method form_valid,which gets the valid form, call the .save() methos on it to save the data to the model.
    # FOR SIMPLE FORM >> We will manuallt create a review instance and save it to the database
    # >> By default the FormView will call the get request and render the form so we don't need any get() method. And to post the data we are using the form_valid method

    form_class = ReviewForm

    model = Review

    template_name = "reviews/review.html"

    success_url = "/thank-you"

    def form_valid(self, form):
        # Creating form data
        user_name = form.cleaned_data["user_name"]
        review_text = form.cleaned_data["review_text"]
        rating = form.cleaned_data["rating"]
        review = Review(user_name=user_name,
                        review_text=review_text, rating=rating)
        review.save()
        return super().form_valid(form)


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
        data = base_query.filter(rating__gte=4)
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


# >> Detail View


class ReviewDetailDetailView(DetailView):
    # To make use of detail view, we have to do 2 things in each case;
    # i) define template name
    # ii) define the Model name that has the data
    # >> Now the Django will automatically dedect the model name and in the template, you can use the context data using the name of the model in lowercase like, "review", or you can use the name "object"
    template_name = "reviews/review_detail.html"

    model = Review

# >> View for sessions and cookies


class AddFavouriteView(View):
    def post(self, request):
        # getting the data from hidden input field
        review_id = request.POST["review_id"]

        # >> this will not work since we cannot store objects in sessoin
        # using that data to search required review
        # fav_review = Review.objects.get(pk=review_id)

        # storing data to a session
        # request.session["favourite_review"] = fav_review

        # Storing object id in session instead whole object since object can't be converted to JSON since it may contain methods
        request.session["favourite_review"] = review_id

        return HttpResponseRedirect(reverse('review-detail', args=[review_id]))
