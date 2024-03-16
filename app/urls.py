"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import Login,Signup,Views,Main,Forgot,Otp,Cnp,Due,Add
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', Login, name='login'),
    path('signup/', Signup, name='signup'),
    path('views/', Views, name='view'),
    path('main/', Main, name='main'),
    path('forget/', Forgot, name='forgot'), 
    path('otp/<str:email>/', Otp, name='otp'),
    path('changepass/<str:email>/', Cnp, name='cnp'),    
    path('dueview/', Due, name='due'),  
    path('add/', Add, name='add'), 

]
