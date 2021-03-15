from django.urls import path

from . import views


app_name = 'tour'

urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'),
    path('guide/', views.GuideView.as_view(), name='guide'),
    path('driver/', views.DriverView.as_view(), name='driver', kwargs={'pk': 1})
]
