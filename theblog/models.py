from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField
from tinymce import models as tinymce_models
from multiselectfield import MultiSelectField
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("adminHome")


choices = Category.objects.all().values_list('name', 'name')
choice_list = []

for item in choices:
    choice_list.append(item)


class MicroSitios(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("adminMicro_list")

class Lectura(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    post_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("adminLectura_list")

class Carousel(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("adminCarousel_list")

class DatosDuros(models.Model):
    title = models.CharField(max_length=255)
    snippet = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.CharField(max_length=255)
    post_date = models.DateField(auto_now_add=True)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("adminDatos_list")  



class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #body = RichTextField(blank=True, null=True)
    #body = models.TextField()
    body = tinymce_models.HTMLField()
    # category = models.CharField(max_length=255, default='Transversal')
    category = MultiSelectField(choices=choice_list)
    snippet = models.CharField(max_length=255)
    post_date = models.DateField(auto_now_add=True)
    fileDownload = models.FileField(null=True, blank=True, upload_to="files/")
    linkToFile = models.CharField(max_length=255, null=True, blank=True)
    past_Publication_Date = models.CharField(max_length=255, null=True, blank=True)

    # objects = PostManager()

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse("adminArticle_list")


class BlogTransversalPost(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #body = RichTextField(blank=True, null=True)
    #body = models.TextField()
    body = tinymce_models.HTMLField()
    # category = models.CharField(max_length=255, default='Transversal')
    category = MultiSelectField(choices=choice_list)
    snippet = models.CharField(max_length=255)
    post_date = models.DateField(auto_now_add=True)
    fileDownload = models.FileField(null=True, blank=True, upload_to="files/")
    linkToFile = models.CharField(max_length=255, null=True, blank=True)
    past_Publication_Date = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse("adminBlogTransversal_list")


class Event(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #body = RichTextField(blank=True, null=True)
    #body = models.TextField()
    body = tinymce_models.HTMLField()
    # category = models.CharField(max_length=255, default='Transversal')
    category = MultiSelectField(choices=choice_list)
    snippet = models.CharField(max_length=255)
    post_date = models.DateField(auto_now_add=True)
    fileDownload = models.FileField(null=True, blank=True, upload_to="files/")
    linkToFile = models.CharField(max_length=255, null=True, blank=True)
    past_Publication_Date = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse("adminEvent_list")


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    conf_num = models.CharField(max_length=15)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.email + " (" + ("not " if not self.confirmed else "") + "confirmed)"
