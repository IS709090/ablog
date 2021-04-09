from django.contrib import admin
from .models import Post, Event, MicroSitios, Category, Lectura, BlogTransversalPost, Subscriber, Profile
# Register your models here. , Carousel, DatosDuros


admin.site.register(Post)
admin.site.register(Event)
admin.site.register(Category)
admin.site.register(MicroSitios)
admin.site.register(BlogTransversalPost)
admin.site.register(Lectura)
# admin.site.register(Carousel)
# admin.site.register(DatosDuros)
admin.site.register(Subscriber)
admin.site.register(Profile)
