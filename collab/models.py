from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    name         = models.CharField(max_length=60)
    email        = models.EmailField(max_length = 254)
    phone_number = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Project(models.Model):
    name        = models.CharField(max_length=60)
    available   = models.BooleanField(default=True)
    description = models.CharField(max_length=1000)
    leader_id   = models.ForeignKey(User, on_delete=models.CASCADE)
    modified    = models.DateTimeField()

    def save(self, *args, **kwargs):
        """On save, update timestamp"""
        self.modified = timezone.now()
        return super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return self.name