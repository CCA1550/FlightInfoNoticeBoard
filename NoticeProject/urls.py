"""NoticeProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from FINB import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.indexRender, name="index"),
    path('notice/', views.noticeRender, name="notice"),
    path('signin/', views.signinRender, name="signin"),
    path('skipping/', views.passwordCheck, name="skipping"),
    # path('error/', views.passwordCheck, name="error"),
    path('release/', views.releaseRender, name="release"),
    path('post/', views.postRelease, name="posyRelease"),
]
