from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField
from tinymce import models as tinymce_models
# Create your models here.

# class Category(models.Model):
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name
    
#     def get_absolute_url(self):
#         return reverse("adminHome")

class MicroSitios(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("adminMicro_list")

# choices = Category.objects.all().values_list('name', 'name')
# choice_list = []

# for item in choices:
#     choice_list.append(item)

class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #body = RichTextField(blank=True, null=True)
    #body = models.TextField()
    body = tinymce_models.HTMLField()
    category = models.CharField(max_length=255, default='Transversal')
    snippet = models.CharField(max_length=255)
    post_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse("adminArticle_list")

class Event(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #body = RichTextField(blank=True, null=True)
    #body = models.TextField()
    body = tinymce_models.HTMLField()
    category = models.CharField(max_length=255, default='Transversal')
    snippet = models.CharField(max_length=255)
    post_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse("adminEvent_list")
