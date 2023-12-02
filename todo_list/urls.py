#comes from the TODOLIST urls.py file
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='abouta'),#name=abouta, abouta is the item referenced on the html files. The about/ is what is referenced in the url when navigating the website
    path('delete/<list_id>',views.delete, name='delete'),#<list_id> allows for the arbitrary naming for the url
    path('cross_off/<list_id>',views.cross_off, name='cross_off'),
    path('uncross/<list_id>',views.uncross, name='uncross'),
    path('edit/<list_id>',views.edit, name='edit'),
]