from django.urls import path

from salesapp import views

urlpatterns = [
    path('', views.login ,name='login'),
    path('signin/', views.signin),
    path('home/', views.home),
    path('add/', views.add_student ,name='add student'),
    path('display/', views.display ,name='display'),
    path('logout/', views.logout),
    path('update/<int:id>/', views.update ,name='update'),
    path('delete/<int:id>/', views.delete,name='delete'),


]