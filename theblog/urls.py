"""ablog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
from . import views
from .views import HomeView, CategoryView, AddCategoryView, ArticleDetailView, AddPostView, EventDetailView, AddEventView, ArticleListView, EventListView, UpdateEventView, UpdatePostView, AdminArticleListView, AdminEventListView, DeleteEventView, DeletePostView, HomeAdminView, DeleteMicroSitioView, UpdateMicroSitioView, AdminMicroSitioListView, AddMicroSitioView, AdminLecturaListView, AddLecturaView, UpdateLecturaView, DeleteLecturaView, AcercaDeListView, ThinkTankListView, BlogTransversalDetailView, BlogTransversalListView, AdminBlogTransversalListView, UpdateBlogTransversalPostView, DeleteBlogTransversalPostView, AddBlogTransversalPostView, SearchView, new, LineasListView, acercaDeDetailView, AddProfileView, DeleteProfileView, UpdateProfileView, AdminProfilesListView
  


urlpatterns = [
    # path('', HomeView.as_view(), name="home_list"),
    # path('admin/', admin.site.urls),
    path('', HomeView, name="home"),
    path('admin/inicio', HomeAdminView.as_view(), name="adminHome"),
    path('admin/publicaciones', AdminArticleListView.as_view(), name="adminArticle_list"),
    path('admin/blogTransversal', AdminBlogTransversalListView.as_view(), name="adminBlogTransversal_list"),
    path('admin/eventos', AdminEventListView.as_view(), name="adminEvent_list"),
    path('admin/perfiles', AdminProfilesListView.as_view(), name="adminProfile_list"),
    # path('admin/datosduros', AdminDatosDurosListView.as_view(), name="adminDatos_list"),
    # path('admin/carrusel', AdminCarouselListView.as_view(), name="adminCarousel_list"),
    path('acercaDe/', AcercaDeListView, name="acercaDe_list"),
    path('acercaDe/<int:pk>/', acercaDeDetailView, name="acercaDe_detail"),
    path('thinktank/', ThinkTankListView, name="think_list"),
    path('admin/lectura', AdminLecturaListView.as_view(), name="adminLectura_list"),
    path('admin/micrositios', AdminMicroSitioListView.as_view(), name="adminMicro_list"),
    path('publicaciones/', ArticleListView, name="article_list"),
    path('blogTransversal/', BlogTransversalListView, name="BlogTransversal_list"),
    path('lineasEstrategicas/', LineasListView, name="lineas"),
    path('eventos/', EventListView, name="event_list"),
    path('categoria/<str:cats>/', CategoryView, name="category"),
    path('busqueda/', SearchView, name="search"),
    path('publicacion/<int:pk>/', ArticleDetailView, name="article-detail"),
    path('blogTransversal/<int:pk>/', BlogTransversalDetailView, name="BlogTransversal-detail"),
    path('evento/<int:pk>/', EventDetailView, name="event-detail"),
    path('admin/crear_evento/', AddEventView.as_view(), name="add_event"),
    # path('admin/crear_carrusel/', AddCarouselView.as_view(), name="add_carousel"),
    path('admin/crear_lectura/', AddLecturaView.as_view(), name="add_lectura"),
    path('admin/crear_perfil/', AddProfileView.as_view(), name="add_profile"),
    path('admin/crear_categoria/', AddCategoryView.as_view(), name="add_category"),
    path('admin/crear_publicacion/', AddPostView.as_view(), name="add_post"),
    path('admin/crear_blogTransversal/', AddBlogTransversalPostView.as_view(), name="add_BlogTransversal"),
    # path('admin/crear_datosduros/', AddDatosView.as_view(), name="add_datos"),
    path('admin/crear_micrositio/', AddMicroSitioView.as_view(), name="add_micro"),
    path('admin/publicacion/editar/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('admin/blogTransversal/editar/<int:pk>', UpdateBlogTransversalPostView.as_view(), name="update_BlogTransversal"),
    # path('admin/carrusel/editar/<int:pk>', UpdateCarouselView.as_view(), name="update_carousel"),
    path('admin/lectura/editar/<int:pk>', UpdateLecturaView.as_view(), name="update_lectura"),
    path('admin/evento/editar/<int:pk>', UpdateEventView.as_view(), name="update_event"),
    path('admin/perfil/editar/<int:pk>', UpdateProfileView.as_view(), name="update_profile"),
    # path('admin/datosduros/editar/<int:pk>', UpdateDatosView.as_view(), name="update_datos"),
    path('admin/micrositio/editar/<int:pk>', UpdateMicroSitioView.as_view(), name="update_micro"),
    path('admin/publicacion/eliminar/<int:pk>', DeletePostView.as_view(), name="delete_post"),
    path('admin/blogTransversal/eliminar/<int:pk>', DeleteBlogTransversalPostView.as_view(), name="delete_BlogTransversal"),
    path('admin/evento/eliminar/<int:pk>', DeleteEventView.as_view(), name="delete_event"),
    # path('admin/datosduros/eliminar/<int:pk>', DeleteDatosView.as_view(), name="delete_datos"),
    path('admin/micrositio/eliminar/<int:pk>', DeleteMicroSitioView.as_view(), name="delete_micro"),
    path('admin/perfil/eliminar/<int:pk>', DeleteProfileView.as_view(), name="delete_profile"),
    # path('admin/carrusel/eliminar/<int:pk>', DeleteCarouselView.as_view(), name="delete_carousel"),
    path('admin/lectura/eliminar/<int:pk>', DeleteLecturaView.as_view(), name="delete_lectura"),
    path('new/', new, name='new'),
]
