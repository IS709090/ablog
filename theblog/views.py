from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Event, MicroSitios, Category, Lectura, Carousel, DatosDuros, User, BlogTransversalPost
from .forms import PostForm, EventForm, MicroSitioForm, CategoryForm, CarouselForm, LecturaForm, DatosDurosForm, BlogTransversalPostForm
from django.urls import reverse_lazy
from itertools import chain

# Create your views here. 

def SearchView(request, search_query):
    print('ok')
    category_posts = Post.objects.filter(category__icontains=search_query).order_by('-id')
    category_events = Event.objects.filter(category__icontains=search_query).order_by('-id')
    title_posts = Post.objects.filter(title__icontains=search_query).order_by('-id')
    title_events = Event.objects.filter(title__icontains=search_query).order_by('-id')
    body_posts = Post.objects.filter(body__icontains=search_query).order_by('-id')
    body_events = Event.objects.filter(body__icontains=search_query).order_by('-id')
    title_blogposts = BlogTransversalPost.objects.filter(title__icontains=search_query).order_by('-id')
    category_blogposts = BlogTransversalPost.objects.filter(category__icontains=search_query).order_by('-id')
    body_blogposts = BlogTransversalPost.objects.filter(body__icontains=search_query).order_by('-id')

    def uniq(iterable):
        seen = set()
        for x in iterable:
            if x in seen:
                continue
            seen.add(x)
            yield x

    finalPosts = uniq(chain(title_posts, body_posts, category_posts))
    finalEvents = uniq(chain(title_events, body_events, category_events))
    finalblogPosts = uniq(chain(title_blogposts, body_blogposts, category_blogposts))
    qs = sorted(finalEvents, key=lambda instance: instance.pk, reverse=True)
    qs2 = sorted(finalPosts, key=lambda instance: instance.pk, reverse=True)
    qs3 = sorted(finalblogPosts, key=lambda instance: instance.pk, reverse=True)

    return render(request, 'search.html', {'search':search_query, 'category_posts':qs2, 'category_posts_events':qs, 'category_blogposts':qs3})


# List



def HomeView(request):
    micros = MicroSitios.objects.all().order_by('-id')
    eventos = Event.objects.all().order_by('-id')
    lecturas = Lectura.objects.all().order_by('-id')
    slides = Carousel.objects.all().order_by('-id')
    datos = DatosDuros.objects.all().order_by('-id')
    blogPost = BlogTransversalPost.objects.all().order_by('-id')
    posts = Post.objects.all().order_by('-id')
    
    search_query = request.GET.get('búsqueda', '')

    if search_query:
        return SearchView(request, search_query)
       
    else:
        return render(request, 'home.html', {'micros':micros, 'eventos':eventos, 'lecturas':lecturas, 'slides':slides, 'datos':datos, 'blogPost':blogPost, 'posts':posts})


def ArticleListView(request):
    posts = Post.objects.all().order_by('-id')
    search_query = request.GET.get('búsqueda', '')

    if search_query:
        return SearchView(request, search_query)
       
    else:
        return render(request, 'article_list.html', {'object_list':posts})


def BlogTransversalListView(request):
    posts = BlogTransversalPost.objects.all().order_by('-id')
    search_query = request.GET.get('búsqueda', '')

    if search_query:
        return SearchView(request, search_query)
       
    else:
        return render(request, 'blogTransversalPost_list.html', {'object_list':posts})


def EventListView(request):
    # model = Event
    # template_name = 'event_list.html'
    # ordering = ['-id']
    # #ordering = ['-post_date']
    posts = Event.objects.all().order_by('-id')
    search_query = request.GET.get('búsqueda', '')

    if search_query:
        return SearchView(request, search_query)
       
    else:
        return render(request, 'event_list.html', {'object_list':posts})


def AcercaDeListView(request):
    # model = User
    # template_name = 'acercaDe_list.html'
    # ordering = ['-id']
    # #ordering = ['-post_date']
    posts = User.objects.all().order_by('-id')
    search_query = request.GET.get('búsqueda', '')

    if search_query:
        return SearchView(request, search_query)
       
    else:
        return render(request, 'acercaDe_list.html', {'object_list':posts})


def LineasListView(request):
    # model = Category
    # template_name = 'lineas.html'
    posts = Category.objects.all().order_by('-id')
    search_query = request.GET.get('búsqueda', '')

    if search_query:
        return SearchView(request, search_query)
       
    else:
        return render(request, 'lineas.html', {'object_list':posts})


def ThinkTankListView(request):
    # model = Category
    # template_name = 'think.html'
    posts = Category.objects.all().order_by('-id')
    search_query = request.GET.get('búsqueda', '')

    if search_query:
        return SearchView(request, search_query)
       
    else:
        return render(request, 'think.html', {'object_list':posts})


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats).order_by('-id')
    category_posts_events = Event.objects.filter(category=cats).order_by('-id')
    category_BlogPost = BlogTransversalPost.objects.filter(category=cats).order_by('-id')
    search_query = request.GET.get('búsqueda', '')

    if search_query:
        return SearchView(request, search_query)
       
    else:
        return render(request, 'categories.html', {'cats':cats, 'category_posts':category_posts, 'category_posts_events':category_posts_events, 'category_blogposts':category_BlogPost})



# Detail

def EventDetailView(request, pk):
    # model = Event
    # template_name = 'event_details.html'
    posts = Event.objects.get(id = pk)
    search_query = request.GET.get('búsqueda', '')
    tags_post = Post.objects.all().order_by('-id')
    tags_events = Event.objects.all().order_by('-id')
    tags_blogp = BlogTransversalPost.objects.all().order_by('-id')

    if search_query:
        return SearchView(request, search_query)
       
    else:
        return render(request, 'event_details.html', {'event':posts, 'post_tag_list':tags_post, 'event_tag_list':tags_events, 'BlogPost_tag_list':tags_blogp})
    # def get_context_data(self, *args, **kwargs):
    #     context = super(EventDetailView, self).get_context_data(*args, **kwargs)
    #     context['post_tag_list'] = Post.objects.all().order_by('-id')
    #     context['event_tag_list'] = Event.objects.all().order_by('-id')
    #     context['BlogPost_tag_list'] = BlogTransversalPost.objects.all().order_by('-id')
    #     return context

    # def get(self, request):
    #     # <view logic>
    #     search_query = request.GET.get('búsqueda', '')
    #     if search_query:
    #         return SearchView(request, search_query)


def ArticleDetailView(request, pk):
    # model = Post
    # template_name = 'article_details.html'
    # def get_context_data(self, *args, **kwargs):
    #     context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
    #     context['post_tag_list'] = Post.objects.all().order_by('-id')
    #     context['event_tag_list'] = Event.objects.all().order_by('-id')
    #     context['BlogPost_tag_list'] = BlogTransversalPost.objects.all().order_by('-id')
    #     return context
    posts = Post.objects.get(id = pk)
    search_query = request.GET.get('búsqueda', '')
    tags_post = Post.objects.all().order_by('-id')
    tags_events = Event.objects.all().order_by('-id')
    tags_blogp = BlogTransversalPost.objects.all().order_by('-id')

    if search_query:
        return SearchView(request, search_query)
       
    else:
        return render(request, 'article_details.html', {'post':posts, 'post_tag_list':tags_post, 'event_tag_list':tags_events, 'BlogPost_tag_list':tags_blogp})


def BlogTransversalDetailView(request, pk):
    # model = BlogTransversalPost
    # template_name = 'blogTransversal_details.html'
    # def get_context_data(self, *args, **kwargs):
    #     context = super(BlogTransversalDetailView, self).get_context_data(*args, **kwargs)
    #     context['post_tag_list'] = Post.objects.all().order_by('-id')
    #     context['event_tag_list'] = Event.objects.all().order_by('-id')
    #     context['BlogPost_tag_list'] = BlogTransversalPost.objects.all().order_by('-id')
    #     return context
    posts = BlogTransversalPost.objects.get(id = pk)
    search_query = request.GET.get('búsqueda', '')
    tags_post = Post.objects.all().order_by('-id')
    tags_events = Event.objects.all().order_by('-id')
    tags_blogp = BlogTransversalPost.objects.all().order_by('-id')

    if search_query:
        return SearchView(request, search_query)
       
    else:
        return render(request, 'blogTransversal_details.html', {'object':posts, 'post_tag_list':tags_post, 'event_tag_list':tags_events, 'BlogPost_tag_list':tags_blogp})




# ADMIN

class HomeAdminView(ListView):
    model = Post
    template_name = 'adminHome.html'

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

class AdminEventListView(ListView):
    model = Event
    template_name = 'adminEvent_list.html'
    ordering = ['-id']
    #ordering = ['-post_date']


# Add

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'


class AddBlogTransversalPostView(CreateView):
    model = BlogTransversalPost
    form_class = BlogTransversalPostForm
    template_name = 'add_BlogTransversal.html'


class AddCategoryView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'add_category.html'


class AddMicroSitioView(CreateView):
    model = MicroSitios
    form_class = MicroSitioForm
    template_name = 'add_micro.html'


class AddEventView(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'add_event.html'


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



#Update

class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    form_class = PostForm


class UpdateBlogTransversalPostView(UpdateView):
    model = BlogTransversalPost
    template_name = 'update_BlogTransversal.html'
    form_class = BlogTransversalPostForm


class UpdateEventView(UpdateView):
    model = Event
    template_name = 'update_event.html'
    form_class = EventForm

class UpdateMicroSitioView(UpdateView):
    model = MicroSitios
    template_name = 'update_micro.html'
    form_class = MicroSitioForm


class UpdateCarouselView(UpdateView):
    model = Carousel
    template_name = 'update_carousel.html'
    form_class = CarouselForm


class UpdateLecturaView(UpdateView):
    model = Lectura
    template_name = 'update_lectura.html'
    form_class = LecturaForm


class UpdateDatosView(UpdateView):
    model = DatosDuros
    template_name = 'update_datos.html'
    form_class = DatosDurosForm


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