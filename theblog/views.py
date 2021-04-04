from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Event, MicroSitios, Category, Lectura, Carousel, DatosDuros, User, BlogTransversalPost
from .forms import PostForm, EventForm, MicroSitioForm, CategoryForm, CarouselForm, LecturaForm, DatosDurosForm, BlogTransversalPostForm
from django.urls import reverse_lazy
# from itertools import chain

# Create your views here. 

#def home(request):
#    return render(request, 'home.html', {})

# List

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    # ordering = ['-post_date']
    ordering = ['-id']
    def get_context_data(self, *args, **kwargs):
        micros = MicroSitios.objects.all().order_by('-id')
        eventos = Event.objects.all().order_by('-id')
        lecturas = Lectura.objects.all().order_by('-id')
        slides = Carousel.objects.all().order_by('-id')
        datos = DatosDuros.objects.all().order_by('-id')
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["micros"] = micros
        context["eventos"] = eventos
        context["lecturas"] = lecturas
        context["slides"] = slides
        context["datos"] = datos
        return context


class HomeAdminView(ListView):
    model = Post
    template_name = 'adminHome.html'


class ArticleListView(ListView):
    model = Post
    template_name = 'article_list.html'
    #ordering = ['-post_date']
    ordering = ['-id']


class BlogTransversalListView(ListView):
    model = BlogTransversalPost
    template_name = 'blogTransversalPost_list.html'
    ordering = ['-id']


class AdminArticleListView(ListView):
    model = Post
    template_name = 'adminArticle_list.html'
    ordering = ['-id']
    #ordering = ['-post_date']


class AdminBlogTransversalListView(ListView):
    model = BlogTransversalPost
    template_name = 'adminBlogTransversal_list.html'
    ordering = ['-id']
    #ordering = ['-post_date']


class AdminCarouselListView(ListView):
    model = Carousel
    template_name = 'adminCarousel_list.html'
    ordering = ['-id']
    #ordering = ['-post_date']


class AdminDatosDurosListView(ListView):
    model = DatosDuros
    template_name = 'adminDatos_list.html'
    ordering = ['-id']
    #ordering = ['-post_date']


class AdminLecturaListView(ListView):
    model = Lectura
    template_name = 'adminLectura_list.html'
    ordering = ['-id']
    #ordering = ['-post_date']


class AdminMicroSitioListView(ListView):
    model = MicroSitios
    template_name = 'adminMicro_list.html'
    ordering = ['-id']
    #ordering = ['-post_date']


class EventListView(ListView):
    model = Event
    template_name = 'event_list.html'
    ordering = ['-id']
    #ordering = ['-post_date']


class AdminEventListView(ListView):
    model = Event
    template_name = 'adminEvent_list.html'
    ordering = ['-id']
    #ordering = ['-post_date']


class AcercaDeListView(ListView):
    model = User
    template_name = 'acercaDe_list.html'
    ordering = ['-id']
    #ordering = ['-post_date']


class LineasListView(ListView):
    model = Category
    template_name = 'lineas.html'


class ThinkTankListView(ListView):
    model = Category
    template_name = 'think.html'


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.capitalize().replace('-', ' ')).order_by('-id')
    category_posts_events = Event.objects.filter(category=cats.capitalize().replace('-', ' ')).order_by('-id')
    category_BlogPost = BlogTransversalPost.objects.filter(category=cats.capitalize().replace('-', ' ')).order_by('-id')
    return render(request, 'categories.html', {'cats':cats.capitalize().replace('-', ' '), 'category_posts':category_posts, 'category_posts_events':category_posts_events, 'category_BlogPost':category_BlogPost})

# def SearchView(request, search):
#     category_posts = Post.objects.filter(category=search.title().replace('-', ' ')).order_by('-id')
#     category_events = Event.objects.filter(category=search.title().replace('-', ' ')).order_by('-id')
#     title_posts = Post.objects.filter(title=search).order_by('-id')
#     title_events = Event.objects.filter(title=search).order_by('-id')
#     body_posts = Post.objects.filter(body=search).order_by('-id')
#     body_events = Event.objects.filter(body=search).order_by('-id')
#     finalPosts = chain(category_posts, title_posts, body_posts)
#     finalEvents = chain(category_events, title_events, body_events)
#     # finalPosts = finalPosts.distinct()
#     # finalEvents = finalEvents.distinct()
#     return render(request, 'search.html', {'search':search.title().replace('-', ' '), 'category_posts':finalPosts, 'category_posts_events':finalEvents})
    

# Add

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'
    #   Para controlar los campos a mostrar
    #   fields = ('title', 'body')


class AddBlogTransversalPostView(CreateView):
    model = BlogTransversalPost
    form_class = BlogTransversalPostForm
    template_name = 'add_BlogTransversal.html'
    #fields = '__all__'
    #   Para controlar los campos a mostrar
    #   fields = ('title', 'body')
    

class AddCategoryView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'add_category.html'
    #fields = '__all__'
    #   Para controlar los campos a mostrar
    #   fields = ('title', 'body')


class AddMicroSitioView(CreateView):
    model = MicroSitios
    form_class = MicroSitioForm
    template_name = 'add_micro.html'
    #fields = '__all__'
    #   Para controlar los campos a mostrar
    #   fields = ('title', 'body')


class AddEventView(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'add_event.html'
    #fields = '__all__'
    #   Para controlar los campos a mostrar
    #   fields = ('title', 'body')


class AddCarouselView(CreateView):
    model = Carousel
    form_class = CarouselForm
    template_name = 'add_carousel.html'


class AddDatosView(CreateView):
    model = DatosDuros
    form_class = DatosDurosForm
    template_name = 'add_datos.html'


class AddLecturaView(CreateView):
    model = Lectura
    form_class = LecturaForm
    template_name = 'add_lectura.html'

# Detail

class EventDetailView(DetailView):
    model = Event
    template_name = 'event_details.html'
    def get_context_data(self, *args, **kwargs):
        context = super(EventDetailView, self).get_context_data(*args, **kwargs)
        context['post_tag_list'] = Post.objects.all().order_by('-id')
        context['event_tag_list'] = Event.objects.all().order_by('-id')
        context['BlogPost_tag_list'] = BlogTransversalPost.objects.all().order_by('-id')
        return context

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'
    def get_context_data(self, *args, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        context['post_tag_list'] = Post.objects.all().order_by('-id')
        context['event_tag_list'] = Event.objects.all().order_by('-id')
        context['BlogPost_tag_list'] = BlogTransversalPost.objects.all().order_by('-id')
        return context


class BlogTransversalDetailView(DetailView):
    model = BlogTransversalPost
    template_name = 'blogTransversal_details.html'
    # def get_context_data(self, *args, **kwargs):
    #     context = super(BlogTransversalDetailView, self).get_context_data(*args, **kwargs)
    #     context['post_tag_list'] = Post.objects.all().order_by('-id')
    #     context['event_tag_list'] = Event.objects.all().order_by('-id')
    #     context['BlogPost_tag_list'] = BlogTransversalPost.objects.all().order_by('-id')
    #     return context


#Update

class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    form_class = PostForm
    #fields = ['title', 'title_tag', 'author', 'category', 'body']


class UpdateBlogTransversalPostView(UpdateView):
    model = BlogTransversalPost
    template_name = 'update_BlogTransversal.html'
    form_class = BlogTransversalPostForm
    #fields = ['title', 'title_tag', 'author', 'category', 'body']


class UpdateEventView(UpdateView):
    model = Event
    template_name = 'update_event.html'
    form_class = EventForm
    #fields = ['title', 'title_tag', 'author', 'category', 'body']

class UpdateMicroSitioView(UpdateView):
    model = MicroSitios
    template_name = 'update_micro.html'
    form_class = MicroSitioForm
    #fields = ['title', 'title_tag', 'author', 'category', 'body']


class UpdateCarouselView(UpdateView):
    model = Carousel
    template_name = 'update_carousel.html'
    form_class = CarouselForm
    #fields = ['title', 'title_tag', 'author', 'category', 'body']


class UpdateLecturaView(UpdateView):
    model = Lectura
    template_name = 'update_lectura.html'
    form_class = LecturaForm
    #fields = ['title', 'title_tag', 'author', 'category', 'body']


class UpdateDatosView(UpdateView):
    model = DatosDuros
    template_name = 'update_datos.html'
    form_class = DatosDurosForm
    #fields = ['title', 'title_tag', 'author', 'category', 'body']


#Delete

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('adminArticle_list')


class DeleteBlogTransversalPostView(DeleteView):
    model = BlogTransversalPost
    template_name = 'delete_BlogTransversal.html'
    success_url = reverse_lazy('adminBlogTransversal_list')


class DeleteEventView(DeleteView):
    model = Event
    template_name = 'delete_event.html'
    success_url = reverse_lazy('adminEvent_list')

class DeleteMicroSitioView(DeleteView):
    model = MicroSitios
    template_name = 'delete_micro.html'
    success_url = reverse_lazy('adminMicro_list')

class DeleteCarouselView(DeleteView):
    model = Carousel
    template_name = 'delete_carousel.html'
    success_url = reverse_lazy('adminCarousel_list')

class DeleteLecturaView(DeleteView):
    model = Lectura
    template_name = 'delete_lectura.html'
    success_url = reverse_lazy('adminLectura_list')


class DeleteDatosView(DeleteView):
    model = DatosDuros
    template_name = 'delete_datos.html'
    success_url = reverse_lazy('adminDatos_list')