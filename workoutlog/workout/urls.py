from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('exercises/', views.exercises, name='exercises'),
    path('getworkouts/', views.getworkouts, name='getworkouts'),
    path('workoutdetail/<int:id>', views.workoutdetail, name='workoutdetail'),
    path('newWorkout', views.newWorkout, name='newWorkout'),
    path('loginmessage', views.loginmessage, name='loginmessage'),
    path('logoutmessage', views.logoutmessage, name='logoutmessage'),
]