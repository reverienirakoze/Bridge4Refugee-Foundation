from django.urls import path
from . import views

urlpatterns= [
    path('', views.home_view, name='contribute'),
    path('get_involved', views.get_involved_view, name='get_involved'),
    path('news_stories', views.news_stories_view, name='news_stories'),
    path('who_we_are', views.who_we_are_view, name='who_we_are'),
    path('our_work', views.our_work_view, name= 'our_work'),
]