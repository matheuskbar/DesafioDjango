from django.urls import path
from django.contrib.auth import views as auth_views
#from usuarios.views.usuario import UsuarioCreate
from usuarios import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #path('cadastrar/', UsuarioCreate.as_view(), name='cadastrar'),
    path('cadastrar/', views.usuario_create, name='cadastrar_usuario'),
    path('meus_dados', views.usuario_read, name='meus_dados'),
    path('update_dados/', views.usuario_update, name='update_dados'),
    path('alterar_senha/', views.alterar_senha, name='alterar_senha'),
    path('recuperar_senha', views.recuperar_senha, name='recuperar_senha'),
]