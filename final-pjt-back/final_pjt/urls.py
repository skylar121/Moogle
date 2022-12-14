"""final_pjt URL Configuration

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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/',include('movies.urls')),
    path('accounts/', include('dj_rest_auth.urls')),
    path('accounts/userinfo/<username>/', views.user_info),
    path('accounts/follow/<username>/', views.follow),
    path('accounts/followers/<username>/', views.followers_list),
    path('accounts/followings/<username>/', views.followings_list),
    path('accounts/signup/',include('dj_rest_auth.registration.urls')),
    path('account/', include('accounts.urls'))
    # path('get_movie/',views.get_movie)
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
