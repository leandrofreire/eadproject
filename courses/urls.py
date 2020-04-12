from django.urls import path


from . import views

app_name='courses'

urlpatterns = [
    path('', views.index, name='index'),
    #path('<int:course_id>/', views.detalhe, name='detalhe'),
    path('<slug:course_slug>/', views.detalhe, name='detalhe'),
    path('<slug:slug>/inscricao/', views.enrollment, name='enrollment')

]