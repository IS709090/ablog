from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Event, MicroSitios, Category, Lectura, User, BlogTransversalPost, Profile
from .forms import PostForm, EventForm, MicroSitioForm, CategoryForm, LecturaForm, BlogTransversalPostForm
from django.urls import reverse_lazy
from itertools import chain
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .models import Subscriber
from .forms import SubscriberForm
import random
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.core.paginator import Paginator

# Create your views here. Carousel CarouselForm DatosDuros DatosDurosForm

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
    all_eventos = Event.objects.all().order_by('-id')
    lecturas = Lectura.objects.all().order_by('-id')
    blogPost = BlogTransversalPost.objects.all().order_by('-id')
    all_posts = Post.objects.all().order_by('-id')

    slidePost = Post.objects.latest('id')
    slideEvent = Event.objects.latest('id')
    slideBlog = BlogTransversalPost.objects.latest('id')

    datos = []
    posts = []
    eventos = []

    # users = User.objects.all().values_list('first_name', 'last_name')
    # choice_list = []

    # for item in users:
    #     choice_list.append(item)
    
    # print(choice_list)
    count = 0
    for blogP in blogPost:
        if count == 3:
            break
        datos.append(blogP)
        count += 1
    
    count = 0
    for blogP in all_posts:
        if count == 3:
            break
        posts.append(blogP)
        count += 1
    
    count = 0
    for blogP in all_eventos:
        if count == 3:
            break
        eventos.append(blogP)
        count += 1
    
    search_query = request.GET.get('búsqueda', '')

    if search_query:
        return SearchView(request, search_query)
       
    else:
        return render(request, 'home.html', {'micros':micros, 'eventos':eventos, 'lecturas':lecturas, 'slidePost':slidePost, 'slideEvent':slideEvent, 'slideBlog':slideBlog, 'datos':datos, 'posts':posts})


def ArticleListView(request):
    posts = Post.objects.all().order_by('-id')
    search_query = request.GET.get('búsqueda', '')
    paginator = Paginator(posts, 5) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if search_query:
        return SearchView(request, search_query)
       
    else:
        return render(request, 'article_list.html', {'object_list':posts, 'page_obj': page_obj})


def BlogTransversalListView(request):
    posts = BlogTransversalPost.objects.all().order_by('-id')
    search_query = request.GET.get('búsqueda', '')
    paginator = Paginator(posts, 5) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if search_query:
        return SearchView(request, search_query)
       
    else:
        return render(request, 'blogTransversalPost_list.html', {'object_list':posts, 'page_obj': page_obj})


def EventListView(request):
    posts = Event.objects.all().order_by('-id')
    search_query = request.GET.get('búsqueda', '')
    paginator = Paginator(posts, 5) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if search_query:
        return SearchView(request, search_query)
       
    else:
        return render(request, 'event_list.html', {'object_list':posts, 'page_obj': page_obj})



def AcercaDeListView(request):
    posts = Profile.objects.all().order_by('-id')
    search_query = request.GET.get('búsqueda', '')

    if search_query:
        return SearchView(request, search_query)
       
    else:
        return render(request, 'acercaDe_list.html', {'object_list':posts})


def LineasListView(request):
    posts = Category.objects.all().order_by('-id')
    search_query = request.GET.get('búsqueda', '')

    if search_query:
        return SearchView(request, search_query)
       
    else:
        return render(request, 'lineas.html', {'object_list':posts})


def ThinkTankListView(request):
    posts = Category.objects.all().order_by('-id')
    search_query = request.GET.get('búsqueda', '')

    if search_query:
        return SearchView(request, search_query)
       
    else:
        return render(request, 'think.html', {'object_list':posts})


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category__contains=cats).order_by('-id')
    category_posts_events = Event.objects.filter(category__contains=cats).order_by('-id')
    category_BlogPost = BlogTransversalPost.objects.filter(category__contains=cats).order_by('-id')
    search_query = request.GET.get('búsqueda', '')

    if search_query:
        return SearchView(request, search_query)
       
    else:
        return render(request, 'categories.html', {'cats':cats, 'category_posts':category_posts, 'category_posts_events':category_posts_events, 'category_blogposts':category_BlogPost})



# Detail

def EventDetailView(request, pk):
    posts = Event.objects.get(id = pk)
    search_query = request.GET.get('búsqueda', '')

    tags_post = []
    tags_events = []
    tags_blogp = []
    
    all_tags_post = Post.objects.all().order_by('-id')
    all_tags_events = Event.objects.all().order_by('-id')
    all_tags_blogp = BlogTransversalPost.objects.all().order_by('-id')

    def uniq(iterable):
        seen = set()
        for x in iterable:
            if x in seen:
                continue
            seen.add(x)
            yield x

    for cat in posts.category:
        for event in all_tags_events:
            for eventCat in event.category:
                if eventCat == cat and event.id != posts.id:
                    tags_events.append(Event.objects.get(id = event.id))
 
    for cat in posts.category:
        for event in all_tags_post:
            for eventCat in event.category:
                if eventCat == cat:
                    tags_post.append(Post.objects.get(id = event.id))
    
    for cat in posts.category:
        for event in all_tags_blogp:
            for eventCat in event.category:
                if eventCat == cat:
                    tags_blogp.append(BlogTransversalPost.objects.get(id = event.id))


    tags_events = uniq(tags_events)
    tags_post = uniq(tags_post)
    tags_blogp = uniq(tags_blogp)

    tags_events = sorted(tags_events, key=lambda instance: instance.pk, reverse=True)
    tags_post = sorted(tags_post, key=lambda instance: instance.pk, reverse=True)
    tags_blogp = sorted(tags_blogp, key=lambda instance: instance.pk, reverse=True)

    tags_events = tags_events[:3]
    tags_post = tags_post[:1]
    tags_blogp = tags_blogp[:1]

    if search_query:
        return SearchView(request, search_query)
       
    else:
        return render(request, 'event_details.html', {'event':posts, 'post_tag_list':tags_post, 'event_tag_list':tags_events, 'BlogPost_tag_list':tags_blogp})


def ArticleDetailView(request, pk):
    posts = Post.objects.get(id = pk)
    search_query = request.GET.get('búsqueda', '')

    tags_post = []
    tags_events = []
    tags_blogp = []
    
    all_tags_post = Post.objects.all().order_by('-id')
    all_tags_events = Event.objects.all().order_by('-id')
    all_tags_blogp = BlogTransversalPost.objects.all().order_by('-id')

    def uniq(iterable):
        seen = set()
        for x in iterable:
            if x in seen:
                continue
            seen.add(x)
            yield x

    for cat in posts.category:
        for event in all_tags_events:
            for eventCat in event.category:
                if eventCat == cat:
                    tags_events.append(Event.objects.get(id = event.id))
 
    for cat in posts.category:
        for event in all_tags_post:
            for eventCat in event.category:
                if eventCat == cat and event.id != posts.id:
                    tags_post.append(Post.objects.get(id = event.id))
    
    for cat in posts.category:
        for event in all_tags_blogp:
            for eventCat in event.category:
                if eventCat == cat:
                    tags_blogp.append(BlogTransversalPost.objects.get(id = event.id))


    tags_events = uniq(tags_events)
    tags_post = uniq(tags_post)
    tags_blogp = uniq(tags_blogp)

    tags_events = sorted(tags_events, key=lambda instance: instance.pk, reverse=True)
    tags_post = sorted(tags_post, key=lambda instance: instance.pk, reverse=True)
    tags_blogp = sorted(tags_blogp, key=lambda instance: instance.pk, reverse=True)

    tags_events = tags_events[:1]
    tags_post = tags_post[:3]
    tags_blogp = tags_blogp[:1]

    if search_query:
        return SearchView(request, search_query)
       
    else:
        return render(request, 'article_details.html', {'post':posts, 'post_tag_list':tags_post, 'event_tag_list':tags_events, 'BlogPost_tag_list':tags_blogp})


def BlogTransversalDetailView(request, pk):
    posts = BlogTransversalPost.objects.get(id = pk)
    search_query = request.GET.get('búsqueda', '')
    
    tags_post = []
    tags_events = []
    tags_blogp = []
    
    all_tags_post = Post.objects.all().order_by('-id')
    all_tags_events = Event.objects.all().order_by('-id')
    all_tags_blogp = BlogTransversalPost.objects.all().order_by('-id')

    def uniq(iterable):
        seen = set()
        for x in iterable:
            if x in seen:
                continue
            seen.add(x)
            yield x

    for cat in posts.category:
        for event in all_tags_events:
            for eventCat in event.category:
                if eventCat == cat:
                    tags_events.append(Event.objects.get(id = event.id))
 
    for cat in posts.category:
        for event in all_tags_post:
            for eventCat in event.category:
                if eventCat == cat:
                    tags_post.append(Post.objects.get(id = event.id))
    
    for cat in posts.category:
        for event in all_tags_blogp:
            for eventCat in event.category:
                if eventCat == cat and event.id != posts.id:
                    tags_blogp.append(BlogTransversalPost.objects.get(id = event.id))
    


    tags_events = uniq(tags_events)
    tags_post = uniq(tags_post)
    tags_blogp = uniq(tags_blogp)

    tags_events = sorted(tags_events, key=lambda instance: instance.pk, reverse=True)
    tags_post = sorted(tags_post, key=lambda instance: instance.pk, reverse=True)
    tags_blogp = sorted(tags_blogp, key=lambda instance: instance.pk, reverse=True)

    tags_events = tags_events[:1]
    tags_post = tags_post[:1]
    tags_blogp = tags_blogp[:3]


    if search_query:
        return SearchView(request, search_query)   
    else:
        return render(request, 'blogTransversal_details.html', {'object':posts, 'post_tag_list':tags_post, 'event_tag_list':tags_events, 'BlogPost_tag_list':tags_blogp})


def acercaDeDetailView(request, pk):
    posts = Profile.objects.get(id = pk)
    search_query = request.GET.get('búsqueda', '')
    
    tags_post = []
    tags_events = []
    tags_blogp = []
    
    all_tags_post = Post.objects.all().order_by('-id')
    all_tags_events = Event.objects.all().order_by('-id')
    all_tags_blogp = BlogTransversalPost.objects.all().order_by('-id')
    all_users = Profile.objects.all().order_by('-id')


    def uniq(iterable):
        seen = set()
        for x in iterable:
            if x in seen:
                continue
            seen.add(x)
            yield x


    for event in all_tags_events:
        for eventCat in event.author:
            if eventCat == posts.full_name:
                tags_events.append(Event.objects.get(id = event.id))
 
    for event in all_tags_post:
        for eventCat in event.author:
            if eventCat == posts.full_name:
                tags_post.append(Post.objects.get(id = event.id))

    for event in all_tags_blogp:
        for eventCat in event.author:
            if eventCat == posts.full_name:
                tags_blogp.append(BlogTransversalPost.objects.get(id = event.id))
    

    tags_events = uniq(tags_events)
    tags_post = uniq(tags_post)
    tags_blogp = uniq(tags_blogp)

    tags_events = sorted(tags_events, key=lambda instance: instance.pk, reverse=True)
    tags_post = sorted(tags_post, key=lambda instance: instance.pk, reverse=True)
    tags_blogp = sorted(tags_blogp, key=lambda instance: instance.pk, reverse=True)



    if search_query:
        return SearchView(request, search_query)   
    else:
        return render(request, 'acercade_details.html', {'object':posts, 'post_tag_list':tags_post, 'event_tag_list':tags_events, 'BlogPost_tag_list':tags_blogp,  'all_users':all_users})


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


# class AdminCarouselListView(ListView):
#     model = Carousel
#     template_name = 'adminCarousel_list.html'
#     ordering = ['-id']
#     #ordering = ['-post_date']


# class AdminDatosDurosListView(ListView):
#     model = DatosDuros
#     template_name = 'adminDatos_list.html'
#     ordering = ['-id']
#     #ordering = ['-post_date']


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


# class AddCarouselView(CreateView):
#     model = Carousel
#     form_class = CarouselForm
#     template_name = 'add_carousel.html'


# class AddDatosView(CreateView):
#     model = DatosDuros
#     form_class = DatosDurosForm
#     template_name = 'add_datos.html'


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


# class UpdateCarouselView(UpdateView):
#     model = Carousel
#     template_name = 'update_carousel.html'
#     form_class = CarouselForm


class UpdateLecturaView(UpdateView):
    model = Lectura
    template_name = 'update_lectura.html'
    form_class = LecturaForm


# class UpdateDatosView(UpdateView):
#     model = DatosDuros
#     template_name = 'update_datos.html'
#     form_class = DatosDurosForm


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

# class DeleteCarouselView(DeleteView):
#     model = Carousel
#     template_name = 'delete_carousel.html'
#     success_url = reverse_lazy('adminCarousel_list')

class DeleteLecturaView(DeleteView):
    model = Lectura
    template_name = 'delete_lectura.html'
    success_url = reverse_lazy('adminLectura_list')


# class DeleteDatosView(DeleteView):
#     model = DatosDuros
#     template_name = 'delete_datos.html'
#     success_url = reverse_lazy('adminDatos_list')


# Helper Functions
def random_digits():
    return "%0.12d" % random.randint(0, 999999999999)

@csrf_exempt
def new(request):
    if request.method == 'POST':
        sub = Subscriber(email=request.POST['email'], conf_num=random_digits())
        sub.save()
        message = Mail(
            from_email=settings.FROM_EMAIL,
            to_emails=sub.email,
            subject='Newsletter Confirmation',
            html_content='Thank you for signing up for my email newsletter! \
                Please complete the process by \
                <a href="{}/confirm/?email={}&conf_num={}"> clicking here to \
                confirm your registration</a>.'.format(request.build_absolute_uri('/confirm/'),
                                                    sub.email,
                                                    sub.conf_num))
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        response = sg.send(message)
        return render(request, 'index.html', {'email': sub.email, 'action': 'added', 'form': SubscriberForm()})
    else:
        return render(request, 'index.html', {'form': SubscriberForm()})