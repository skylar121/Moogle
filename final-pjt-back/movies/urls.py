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
from django.urls import path
from . import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('get_movie/',views.get_movie),
    path('get_genre/',views.get_genre),
    path('',views.movie_list),
    path('<int:tmdb_id>/',views.movie_detail),
    path('goto_main/',views.goto_main),
    path('action10',views.action10),
    #drf-spectacular
    path('schema/', SpectacularAPIView.as_view(),name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'),name='swagger-ui')
    # path('action20/',views.action20),
]
