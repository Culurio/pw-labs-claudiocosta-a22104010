from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('licenciatura', views.licenciatura_page_view, name='licenciatura'),
    path('projetos', views.projects_page_view, name='projetos'),
    path('blog', views.view_new_post, name='blog'),
    path('login', views.login_view, name='login'),
    path('logout', views.view_logout, name='logout'),
]