from . import views
from django.urls import path
app_name='challengeapp'
urlpatterns = [
    path('add/',views.addition,name='add'),
    #path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
   # path('home',views.home,name='home'),
    path('contact/', views.contact, name='contact'),

    path('thanks/', views.thanks, name='thanks'),
    path('',views.demo,name='demo'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
  #  path('moviedetails',views.moviedetails,name='moviedetails'),
   # path('add/',views.add,name='add'),
   # path('update/<int:id>/',views.update,name='update')



]
