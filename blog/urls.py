from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    # path('', index, name='home'),
    path('', HomeNews.as_view(), name='home'),
    # path('category/<int:category_id>/', get_categories, name='category'),
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='category'),
    # path('blog/<int:news_id>/', view_news, name='view_news'),
    path('blog/<int:pk>/', ViewNews.as_view(), name='view_news'),
    # path('blog/add_news/', add_news, name='add_news'),
    path('blog/add_news/', CreateNews.as_view(), name='add_news'),
    path('blog/contact/', contact, name='contact')
]
