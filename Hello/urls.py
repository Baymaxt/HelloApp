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
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls')),
    path('', include('chat.urls')),
    path('', include('home.urls')),
    path('', include('quanquan.urls')),
    path('', include('personal_center.urls')),
    # 接口文档地址
    # MarkupSafe-1.1.1 certifi-2020.4.5.1 chardet-3.0.4 coreapi-2.3.3 coreschema-0.0.4
    # idna-2.9 itypes-1.2.0 jinja2-2.11.2 requests-2.23.0 uritemp
    # late-3.0.1 urllib3-1.25.9
    path('docs/', include_docs_urls(title='My API title')),
]
