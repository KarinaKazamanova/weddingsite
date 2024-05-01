"""
URL configuration for wedding project.

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
from django.urls import path, include
from wedding_invitation import views
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('mother/', mom, name='mother'),
    path('father/', father, name='father'),
    path('j&a/', julia_and_artem, name='julia and artem'),
    path('gasan/', gasan, name='gasan'),
    path('nikita/', nikita, name='nikita'),
    path('maria/', maria, name='maria'),
    path('anna/', anna, name='anna'),
    path('a&i/', alexandr_and_irina, name='alexandr and irina'),
    path('a&l/', aina_and_latifa, name='aina and latifa'),
    path('sveta/', sveta, name='sveta'),
    path('n&o/', nikita_and_olya, name='nikita and olya'),
    path('tatiana/', tatiana, name='tatiana'),
    path('egor/', egor, name='egor'),
    path('tatiana/', tatiana, name='tatiana'),
    
    
    
    
    
]
