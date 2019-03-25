from django.urls import path
from . import views

app_name = 'Brexit'

urlpatterns = [
	path('', views.index, name='index'),
	path('search/brexit', views.search_quotes, name='search_brexit'),
	path('search/form', views.search_form, name='search_form'),
]
