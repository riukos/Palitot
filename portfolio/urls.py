# portfolio/urls.py
from django.urls import path
from .views import home, about, project_list, project_detail

app_name = 'portfolio'

urlpatterns = [
    path('', project_list, name='project_list'),
    path('about/', about, name='about'),
    path('projects/', project_list, name='project_list'),
    path('projects/<int:projeto_id>/', project_detail, name='project_detail'),
]
