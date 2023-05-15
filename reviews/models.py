from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator

# Create your models here.


class Review(models.Model):
    user_name = models.CharField(max_length=50)
    review_text = models.TextField(max_length=200)
    rating = models.IntegerField(
        validators=[MinLengthValidator(1), MaxLengthValidator(5)])

    def __str__(self):
        return f"{self.user_name}, {self.review_text}, {self.rating}"


class Complain(models.Model):
    user_name = models.CharField(max_length=50)
    complain_text = models.TextField(max_length=300)
    order_id = models.CharField(max_length=6)

    def __str__(self):
        return f"{self.user_name}, {self.order_id}"
