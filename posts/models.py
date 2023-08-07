from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import redirect


# Create your models here.

class PostModel(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='post_images')
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    date_edit = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    def get_author(self):
        return self.author.username

    def get_absolute_url(self):
        return redirect('detail', arg=[str(self.pk)])

