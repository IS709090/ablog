from django import forms
from .models import Post, Event, MicroSitios, Category

choices = Category.objects.all().values_list('name', 'name')
choice_list = []

for item in choices:
    choice_list.append(item) 

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'snippet', 'header_image', 'category', 'body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título de la publicación'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título de la publicación que veremos en la pestaña'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'type': 'hidden', 'id': 'user'}),            
            #'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Autor de la publicación'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control', 'placeholder': 'Categorías de la publicación'}),
            'header_image': forms.ClearableFileInput(attrs={'class': 'form-control', 'required' : '' , 'placeholder': 'Imágen'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción o resumen de la publicación, que saldrá debajo de la publicación en el listado de publicaciones'}),
            #'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Contenido de la publicación'}),
        }

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'title_tag', 'author', 'snippet', 'header_image', 'category', 'body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título del evento'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título del evento que veremos en la pestaña'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'type': 'hidden', 'id': 'user'}),
            #'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Autor del evento'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control', 'placeholder': 'Categorías del evento'}),
            'header_image': forms.ClearableFileInput(attrs={'class': 'form-control', 'required' : '' , 'placeholder': 'Imágen'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción o resumen del evento, que saldrá debajo del evento en el listado de eventos'}),
            #'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Contenido del evento'}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la categoría'}),
        }

class MicroSitioForm(forms.ModelForm):
    class Meta:
        model = MicroSitios
        fields = ('title', 'header_image', 'link')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título del Micrositio'}),
            'link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enlace al Micrositio'}),
            'header_image': forms.ClearableFileInput(attrs={'class': 'form-control', 'required' : '' , 'placeholder': 'Imágen'}),
        }