from django import forms
from .models import Post, Event, MicroSitios, Category, Lectura, BlogTransversalPost, User, Profile

# Carousel, DatosDuros,


MY_CHOICES = (('item_key1', 'Item title 1.1'),
              ('item_key2', 'Item title 1.2'),
              ('item_key3', 'Item title 1.3'),
              ('item_key4', 'Item title 1.4'),
              ('item_key5', 'Item title 1.5'))

choices = Category.objects.all().values_list('name', 'name')
choice_list = []

for item in choices:
    choice_list.append(item)

users = Profile.objects.all().values_list('full_name', 'full_name')
users_choice_list = []

for item in users:
    users_choice_list.append(item)

class SubscriberForm(forms.Form):
    email = forms.EmailField(label='Your email',
                             max_length=100,
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'optional_author', 'snippet', 'header_image', 'fileDownload', 'linkToFile', 'past_Publication_Date', 'category', 'body')
        category = forms.ChoiceField(choices=choice_list)
        author = forms.ChoiceField(choices=users_choice_list)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título de la publicación'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título de la publicación que veremos en la pestaña'}),
            'optional_author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Autores que no salen en la lista. Si son varios, sepáralos con coma'}),
            # 'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Autor de la publicación'}),
            'header_image': forms.ClearableFileInput(attrs={'class': 'form-control', 'required' : '' , 'placeholder': 'Imágen'}),
            'fileDownload': forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'OPCIONAL. Archivo a descargar'}),
            'linkToFile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'OPCIONAL. Enlace a archivo descargable, si está almacenado en otra plataforma'}),
            'past_Publication_Date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'OPCIONAL. Fecha antigua de publicación, solo usar cuando se este migrando todo, ignorar si es publicación nueva. Formato Ejemplo: 7 de Abril de 2021'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción o resumen de la publicación, que saldrá debajo de la publicación en el listado de publicaciones'}),
        }



class BlogTransversalPostForm(forms.ModelForm):
    class Meta:
        model = BlogTransversalPost
        fields = ('title', 'title_tag', 'author', 'optional_author', 'snippet', 'header_image', 'fileDownload', 'linkToFile', 'past_Publication_Date', 'category', 'body')
        category = forms.ChoiceField(choices=choice_list)
        author = forms.ChoiceField(choices=users_choice_list)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título del Blog'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título del Blog que veremos en la pestaña'}),
            'optional_author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Autores que no salen en la lista. Si son varios, sepáralos con coma'}),
            # 'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Autor del Blog'}),
            'header_image': forms.ClearableFileInput(attrs={'class': 'form-control', 'required' : '' , 'placeholder': 'Imágen'}),
            'fileDownload': forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'OPCIONAL. Archivo a descargar'}),
            'linkToFile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'OPCIONAL. Enlace a archivo descargable, si está almacenado en otra plataforma'}),
            'past_Publication_Date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'OPCIONAL. Fecha antigua de publicación, solo usar cuando se este migrando todo, ignorar si es publicación nueva. Formato Ejemplo: 7 de Abril de 2021'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción o resumen del Blog, que saldrá debajo del Blog en el listado de Blog'}),
        }



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user', 'full_name', 'rol', 'bio', 'profile_pic', 'twitter', 'facebook', 'linkedin', 'instagram', 'youtube')
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control', 'required' : '' , 'placeholder': 'Usuario al que se le asignará el perfil'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'required' : '' , 'placeholder': 'Nombre completo'}),
            'rol': forms.TextInput(attrs={'class': 'form-control', 'required' : '' , 'placeholder': 'Rol en TRANSVERSAL'}),
            # 'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Autor del Blog'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'required' : '' , 'placeholder': 'Biografía'}),
            'profile_pic': forms.ClearableFileInput(attrs={'class': 'form-control', 'required' : '' , 'placeholder': 'Imágen'}),
            'twitter': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'OPCIONAL.'}),
            'facebook': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'OPCIONAL.'}),
            'linkedin': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'OPCIONAL.'}),
            'instagram': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'OPCIONAL.'}),
            'youtube': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'OPCIONAL.'}),
        }




class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'title_tag', 'author', 'optional_author', 'snippet', 'header_image', 'fileDownload', 'linkToFile', 'past_Publication_Date', 'category', 'body')
        category = forms.ChoiceField(choices=choice_list)
        author = forms.ChoiceField(choices=users_choice_list)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título del evento'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título del evento que veremos en la pestaña'}),
            'optional_author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Autores que no salen en la lista. Si son varios, sepáralos con coma'}),
            # 'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Autor del evento'}),
            'header_image': forms.ClearableFileInput(attrs={'class': 'form-control', 'required' : '' , 'placeholder': 'Imágen'}),
            'fileDownload': forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'OPCIONAL. Archivo a descargar'}),
            'linkToFile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'OPCIONAL. Enlace a archivo descargable, si está almacenado en otra plataforma'}),
            'past_Publication_Date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'OPCIONAL. Fecha antigua de publicación, solo usar cuando se este migrando todo, ignorar si es publicación nueva. Formato Ejemplo: 7 de Abril de 2021'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción o resumen del evento, que saldrá debajo del evento en el listado de eventos'}),
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
        fields = ('title', 'description','header_image', 'fileDownload', 'link')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título de la lectura'}),
            'link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'OPCIONAL. Enlace a la lectura'}),
            'header_image': forms.ClearableFileInput(attrs={'class': 'form-control', 'required' : '' , 'placeholder': 'Imágen'}),
            'fileDownload': forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'OPCIONAL. Archivo a descargar'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción o resumen de la lectura'}),
        }

