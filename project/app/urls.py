from django.contrib import admin
from django.urls import path
from django.urls import path
from .views import index,like
urlpatterns = [
     #path('', index,name='index'),
    #path('search-products', ajax_search_products, name='ajax-search'),
    #path('ajax/search-products', ajax_search_products, name='ajax-search'),
     path('', index, name='index'),
     path('like/',like, name='like'),
     # path('search',search,name='search')


]