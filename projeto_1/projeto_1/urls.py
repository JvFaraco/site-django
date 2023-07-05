
from django.urls import path
from cadastro_usuarios import views
urlpatterns = [
    #rota, view responsável, nome de referência
    #dentro do path 'facebook.com/('path')'
    path('',views.home,name='home'),
    #usuarios.com/usuarios
    path('usuarios/',views.usuarios,name='listagem_usuarios'),
    path('link/,', views.link, name='link')

]