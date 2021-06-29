from django.db import models


# Create your models here.
class user(models.Model):
    name = models.CharField( max_length=50, null=False)
    dob = models.DateField()
    telephone = models.CharField( max_length=130, null=True, blank=True)
    email = models.EmailField( null=True, blank=True)
    def __str__(self):
            return self.name