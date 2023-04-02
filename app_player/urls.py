from django.contrib import admin
from django.urls import path
from app_player.views import PlayerView, SongCreateView, SongUpdateView, SongDeleteView, LooperUpdateView
from app_player.views import looper, looper_with_param, index

from app_player.models import Song, Part


# admin.site.register(Song)  # appear in admin form after registration
# admin.site.register(Part)

urlpatterns = [
    path('', index, name='index'),
    path('songs_list', PlayerView.as_view(), name='songs_list'),
    path('song/add_song', SongCreateView.as_view(), name='add_song'),
    path('song/update_song/<pk>', SongUpdateView.as_view(), name='update_song'),
    path('song/delete_song/<pk>', SongDeleteView.as_view(), name='delete_song' ),
    path('looper_with_param/<song_url>/<int:start_p>/<int:stop_p>/', looper_with_param, name='loop_it'),
    path('looper_update/<pk>', LooperUpdateView.as_view(), name='looper_update'),
    path('looper/<pk>', looper, name='looper'),
    # path('log_in/', PlayerView.as_view(), name='index'),
]
