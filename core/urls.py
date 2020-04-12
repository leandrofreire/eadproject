from django.urls import path

from . import views

app_name='core'

urlpatterns = [
    path('', views.index, name='inicio'),
    path('contato', views.contato, name='contato'),
    path('sobre', views.sobre, name='sobre'),
]