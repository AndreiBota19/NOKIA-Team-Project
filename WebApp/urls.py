from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = 'webapp-home'),
    path('about/', views.about, name = 'webapp-about'),
    path('viewData/', views.viewData, name = 'webapp-viewData'),


]
