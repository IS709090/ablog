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

MY_CHOICES = (('item_key1', 'Item title 1.1'),
              ('item_key2', 'Item title 1.2'),
              ('item_key3', 'Item title 1.3'),
              ('item_key4', 'Item title 1.4'),
              ('item_key5', 'Item title 1.5'))

# choices = Category.objects.all().values_list('name', 'name')
# choice_list = []

# for item in choices:
#     choice_list.append(item)

users = User.objects.all().values_list('first_name', 'last_name')
users_choice_list = []

for item in users:
    users_choice_list.append(item)


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

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    rol = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    twitter = models.CharField(max_length=255, null=True, blank=True)
    facebook = models.CharField(max_length=255, null=True, blank=True)
    linkedin = models.CharField(max_length=255, null=True, blank=True)
    instagram = models.CharField(max_length=255, null=True, blank=True)
    youtube = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)

class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    title_tag = models.CharField(max_length=255)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    author = MultiSelectField(choices=users_choice_list)
    #body = RichTextField(blank=True, null=True)
    #body = models.TextField()
    body = tinymce_models.HTMLField()
    # category = models.CharField(max_length=255, default='Transversal')
    category = MultiSelectField(choices=MY_CHOICES)
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
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    author = MultiSelectField(choices=users_choice_list)
    #body = RichTextField(blank=True, null=True)
    #body = models.TextField()
    body = tinymce_models.HTMLField()
    # category = models.CharField(max_length=255, default='Transversal')
    category = MultiSelectField(choices=MY_CHOICES)
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
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    author = MultiSelectField(choices=users_choice_list)
    #body = RichTextField(blank=True, null=True)
    #body = models.TextField()
    body = tinymce_models.HTMLField()
    # category = models.CharField(max_length=255, default='Transversal')
    category = MultiSelectField(choices=MY_CHOICES)
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
