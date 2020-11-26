from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=254)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=True)  # validators should be a list

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=60)
    available = models.BooleanField(default=True)
    description = models.CharField(max_length=1000)
    leader_id = models.ForeignKey(User, on_delete=models.CASCADE)
    modified = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        """On save, update timestamp"""
        self.modified = timezone.now()
        return super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
