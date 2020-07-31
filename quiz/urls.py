from django.urls import path

from quiz import views

app_name = 'quiz'

urlpatterns = [
    path('', views.main, name='main'),
    path('index/', views.index, name='index'),
    path('results/', views.results, name='results'),
    path('list/', views.list, name='list'),
]


