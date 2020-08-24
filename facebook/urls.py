"""facebook URL Configuration

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
from django.urls import path,include
from authentication import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path("",views.home,name="home"),
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("register/", views.registerPage, name="register"),
    path("perfil/", views.profileUpdateView.as_view(), name="profile"),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path('agenda/', include('schedule.urls')),
    path('no_autorizado/', views.NoAuthorize.as_view(),name="no_authorize"),
]
