from django import forms
from .models import Complain


class ReviewForm(forms.Form):
    user_name = forms.CharField(
        label="Your Name", max_length=50, required=True, error_messages={
            "required": "Your name must not be empty",
            "max_length": "Please enter shorter name"
        })
    review_text = forms.CharField(
        label="Your Field", widget=forms.Textarea, max_length=200)
    rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)

# >> Creating model forms


class ComplainForm(forms.ModelForm):
    class Meta:
        model = Complain
        fields = "__all__"  # include all model fields as form fields
        # exclude = ['customer_id']
        labels = {
            "user_name": "Your Name",
            "complain_text": "What bother you?",
            "order_id": "Order ID (complain order)"
        }
        error_messages = {
            "user_name": {
                "required": "Please fill all the fields",
                "max_length": "Please don't exceed the word limit"
            }
        }
