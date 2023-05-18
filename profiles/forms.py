from django.forms import forms


class FileForm(forms.Form):
    user_image = forms.FileField()
