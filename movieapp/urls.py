
from django.contrib import admin
from django.urls import path


from . import views 


urlpatterns = [
    path('', views.mainview),
    path('login', views.login),
    path('main2', views.main2),
    path('quest/', views.quest),
    path('test1/', views.test1),

]
