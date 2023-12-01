from django.db import models

# Create your models here.


class Post(models.Model):
    body = models.TextField()
    title = models.CharField(max_length=200,null=True)

    def __str__(self) -> str:
        return f"Post({self.body[:30]}...)"


