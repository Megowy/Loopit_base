"""Player URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from app_player.models import Song, Part
from app_player.views import PlayerView, SongCreateView, SongUpdateView, LooperUpdateView
from app_player.views import  looper, looper_with_param

admin.site.register(Song)  # appear in admin form after registration
admin.site.register(Part)

urlpatterns = [
    path('', PlayerView.as_view(), name='index'),
    path('looper/<s_id>', looper, name='looper'),
    # path('looper_update/'),
    path('song/add_song', SongCreateView.as_view(), name='add_song'),
    path('song/update_song/<pk>', SongUpdateView.as_view(), name='update_song'),
    path('looper_with_param/<song_url>/<int:start_p>/<int:stop_p>/', looper_with_param, name='loop_it'),
    path('admin/', admin.site.urls),
    path('log_in/', PlayerView.as_view(), name='index'),
    path('loper_update/<p_id>', LooperUpdateView.as_view(), name='looper_update')
    # path('part/')
]
