from django.urls import path

from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.index, name='index'),
    # path('<int:course_id>/', views.detalhe, name='detalhe'),
    path('<slug:course_slug>/', views.detalhe, name='detalhe'),
    path('<slug:slug>/inscricao/', views.enrollment, name='enrollment'),
    path('<slug:slug>/anuncios/', views.announcements, name='announcements'),
    path('<slug:slug>/anuncios/<int:pk>/', views.show_announcement, name='show_announcement'),
    path('<slug:slug>/cancelar-inscricao/', views.undo_enrollment, name='undo_enrollment')

]
