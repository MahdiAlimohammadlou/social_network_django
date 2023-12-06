from django.db import models

# Create your models here.
class UserProfile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    job = models.CharField(max_length=50)
    company = models.CharField(max_length=20)
    city = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f"Post({self.first_name} {self.last_name})"
