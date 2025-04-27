from django.urls import path
from . import views

urlpatterns = [
    path('contribute', views.contribute_view, name='contribute'),
    path('get_involved', views.get_involved_view, name='get_involved'),
    path('', views.home_view, name='news_stories'),
    path('who_we_are', views.who_we_are_view, name='who_we_are'),
    path('our_work', views.our_work_view, name='our_work'),
    path('news/', views.news_stories, name='news_stories'),
    path('stories/', views.story_list, name='story_list'),
]