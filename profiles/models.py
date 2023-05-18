from django.db import models

# Create your models here.


class UserProfile(models.Model):
    # BASIC IDEA >> So, we do not ideally store the image on the DB, we only store the path on the DB and Django saves the image in one of our folders in our project folder. We specify the folder by creating it manually and then declaring anew setting in the settings.py " MEDIA_ROOT = BASE_DIR / "uploads" ". Through upload_to, a new sub-folder in uploads wwill be created with the name of images in which all the images of this input field will be saved

    # >> Using a FileField that accepts all file types
    # image = models.FileField(upload_to="images")

    # >> Using an ImageField that accepts only image files, uses an extra library "Pillow"
    image = models.ImageField(upload_to="images")
