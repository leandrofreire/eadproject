from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views
app_name = 'accounts'

urlpatterns = [
    path('entrar/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('sair/', LogoutView.as_view(next_page='core:inicio'), name='login'),
    path('cadastrar/', views.register, name='register'),
    path('password_reset/', views.password_reset, name='password_reset'),
    path('editar/', views.edit, name='edit'),
    path('editar-senha/', views.edit_password, name='edit_password'),
    path('confirmar\\-senha/(?P<key>[0-9]+)$', views.password_reset_confirm, name='password_reset_confirm'),
    path('', views.dashboard, name='dashboard')
]
