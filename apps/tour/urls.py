
from django.urls import path
from django.conf.urls import url
from . import views


app_name = 'tour'

urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'),
    path('guide/', views.GuideView.as_view(), name='guide'),
    path('driver/', views.DriverView.as_view(), name='driver', kwargs={'pk': 1}),
    #path('guide/',views.light_view),
    #url(r'^guide/',views.light_view), 
    path('guide/turn_on/',views.turn_on),
    path('guide/turn_off/',views.turn_off),
    path('guide/refresh/',views.refresh),
  
    #url(r'^guide/',views.GuideView.as_view()), 
    #url(r'^turn_on/',views.turn_on), 
    #url(r'^turn_off/',views.turn_off),
    #url(r'^refresh/',views.refresh),
]
