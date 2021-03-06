"""Hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from personal import views

app_name = 'personal'
urlpatterns = [
    path('personal/', views.PersonalViews.as_view(), name='personal'),
    path('personal/', include('personal_interaction.urls')),
    path('personal/', include('personal_tools.urls')),
    path('personal/', include('personal_sub_black.urls')),
    path('personal/', include('personal_setting.urls')),
]
