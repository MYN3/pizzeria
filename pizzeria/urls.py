from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^$', views.lista_peliculas, name ='lista_peliculas'),
    url(r'^$', views.pizza_lista, name='pizza_lista'),
    url(r'^pizza/(?P<pk>[0-9]+)/$', views.pizza_detail,  name='pizza_detail'),
    url(r'^pizza/(?P<pk>[0-9]+)/editar/$', views.pizza_editar, name='pizza_editar'),
    url(r'^pizza/nueva/$', views.pizza_nueva, name='pizza_nueva'),
    url(r'^ingrediente/lista/$', views.ingrediente_lista, name='ingrediente_lista'),
    url(r'^ingrediente/nuevo/$', views.ingrediente_nuevo, name='ingrediente_nuevo'),
    url(r'^pizza/(?P<pk>\d+)/remove/$', views.pizza_remove, name='pizza_remove'),
    ]
