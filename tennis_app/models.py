from django.db import models

# Create your models here.
from django.db import models

class Tournament(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    location = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Venue(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=50, default='No phone number provided')
    schedule = models.CharField(max_length=255, default='No schedule available')
    image = models.ImageField(null=True, blank=True)
    # description = models.TextField()

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Course(models.Model):
    name = models.CharField(max_length=255)
    instructor = models.CharField(max_length=255)
    schedule = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
