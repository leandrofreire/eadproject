from django.urls import path

from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.index, name='index'),
    path('criar_curso/', views.criar_curso, name='criar_curso'),
    # path('<int:course_id>/', views.detalhe, name='detalhe'),
    path('<slug:course_slug>/', views.detalhe, name='detalhe'),
    path('<slug:slug>/inscricao/', views.enrollment, name='enrollment'),
    path('<slug:slug>/anuncios/', views.announcements, name='announcements'),
    path('<slug:slug>/aulas/', views.lessons, name='lessons'),
    path('<slug:slug>/aulas/<int:pk>/', views.lesson, name='lesson'),
    path('<slug:slug>/materiais/<int:pk>/', views.material, name='material'),
    path('<slug:slug>/anuncios/<int:pk>/', views.show_announcement, name='show_announcement'),
    path('<slug:slug>/cancelar-inscricao/', views.undo_enrollment, name='undo_enrollment')

]
