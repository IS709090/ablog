from django import forms
from .models import Post, Event, MicroSitios, Category, Lectura, Carousel, DatosDuros, BlogTransversalPost

choices = Category.objects.all().values_list('name', 'name')
choice_list = []

for item in choices:
    choice_list.append(item) 

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'snippet', 'header_image', 'category', 'body')
        category = forms.ChoiceField(choices=choice_list)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título de la publicación'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título de la publicación que veremos en la pestaña'}),
            'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Autor de la publicación'}),
            # 'category': forms.MultipleChoiceField(choices=choice_list),
            # 'category': forms.ChoiceField(choices=choice_list, widget=forms.Select(attrs={'class':'bootstrap-select'})),
            'header_image': forms.ClearableFileInput(attrs={'class': 'form-control', 'required' : '' , 'placeholder': 'Imágen'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción o resumen de la publicación, que saldrá debajo de la publicación en el listado de publicaciones'}),
            #'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Contenido de la publicación'}), attrs={'class': 'form-control', 'placeholder': 'Categorías de la publicación'}
        }


class BlogTransversalPostForm(forms.ModelForm):
    class Meta:
        model = BlogTransversalPost
        fields = ('title', 'title_tag', 'author', 'snippet', 'header_image', 'category', 'body')
        category = forms.ChoiceField(choices=choice_list)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título del Blog'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título del Blog que veremos en la pestaña'}),
            'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Autor del Blog'}),
            # 'category': forms.Select(choices=choice_list, attrs={'class': 'form-control', 'placeholder': 'Categorías del Blog'}),
            'header_image': forms.ClearableFileInput(attrs={'class': 'form-control', 'required' : '' , 'placeholder': 'Imágen'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción o resumen del Blog, que saldrá debajo del Blog en el listado de Blog'}),
            #'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Contenido de la publicación'}),
        }


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'title_tag', 'author', 'snippet', 'header_image', 'category', 'body')
        category = forms.ChoiceField(choices=choice_list)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título del evento'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título del evento que veremos en la pestaña'}),
            'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Autor del evento'}),
            # 'category': forms.Select(choices=choice_list, attrs={'class': 'form-control', 'placeholder': 'Categorías del evento'}),
            'header_image': forms.ClearableFileInput(attrs={'class': 'form-control', 'required' : '' , 'placeholder': 'Imágen'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción o resumen del evento, que saldrá debajo del evento en el listado de eventos'}),
            #'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Contenido del evento'}),
        }


class DatosDurosForm(forms.ModelForm):
    class Meta:
        model = DatosDuros
        fields = ('title', 'author', 'snippet', 'header_image', 'link')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título del Dato'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción o resumen del Dato'}),
            'link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enlace al que te lleva'}),
            'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Autor del Dato'}),
            'header_image': forms.ClearableFileInput(attrs={'class': 'form-control', 'required' : '' , 'placeholder': 'Imágen'}),
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


class LecturaForm(forms.ModelForm):
    class Meta:
        model = Lectura
        fields = ('title', 'description','header_image', 'link')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título de la lectura'}),
            'link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enlace a la lectura'}),
            'header_image': forms.ClearableFileInput(attrs={'class': 'form-control', 'required' : '' , 'placeholder': 'Imágen'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción o resumen de la lectura'}),
        }


class CarouselForm(forms.ModelForm):
    class Meta:
        model = Carousel
        fields = ('title', 'subtitle','header_image', 'link')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título del Slide'}),
            'subtitle': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Subtítulo del Slide'}),
            'link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enlace a la publicación/evento del Slide'}),
            'header_image': forms.ClearableFileInput(attrs={'class': 'form-control', 'required' : '' , 'placeholder': 'Imágen'}),   
        }