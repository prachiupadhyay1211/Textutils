"""
URL configuration for textutils project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from .import views

# code for 1st part (just opening website-codewithharry)
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.index, name='index'),
#     path('about/', views.about, name='about'),
# ]

# code for laying of pipeline
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('analyze/', views.analyze, name='analyze'),
    path('', views.index, name='home')


    # path('removepunc/', views.removepunc, name='rempun'),
    # path('capitalizefirst/', views.capitalizefirst, name='capfirst'),
    # path('newlineremove/', views.newlineremove, name='newlineremove'),
    # path('spaceremove/', views.spaceremove, name='spaceremove'),
    # path('charcount', views.charcount, name='charcount'),
]
