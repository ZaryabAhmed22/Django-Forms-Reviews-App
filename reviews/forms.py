from django import forms


class ReviewForm(forms.Form):
    user_name = forms.CharField(max_length=50, required=True)
