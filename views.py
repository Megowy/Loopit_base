from logging import getLogger
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from app_player.models import Song, Part
from app_player.forms import SongForm, PartForm
from app_player.additon import get_length


LOGGER = getLogger()

def index(request):
    return render(request, template_name='index.html')

class PlayerView(ListView):
    template_name = 'songs.html'
    model = Song
    def get_queryset(self):
        return Song.objects.filter(user=self.request.user)


class SongCreateView(CreateView):
    model = Song
    template_name = 'form.html'
    form_class = SongForm
    success_url = reverse_lazy('songs_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return  super().form_valid(form)

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data.')
        return super().form_invalid(form)

    # def get_queryset(self):
    #     return Song.objects.filter(user=self.request.user)


class SongUpdateView(UpdateView):
    template_name = 'form.html'
    model = Song
    form_class = SongForm
    success_url = reverse_lazy('songs_list')

class SongDeleteView(DeleteView):
    template_name = 'delete_song_confirmation.html'
    model = Song
    success_url = reverse_lazy('songs_list')


class LooperUpdateView(UpdateView):
    template_name = 'looper_update.html'
    model = Part
    form_class = PartForm



def looper(request, pk):
    urlval = Song.objects.get(id=pk).song_url
    parts = Part.objects.filter(song_id=pk).values('start_p', 'stop_p')

    length_sec = get_length(urlval)

    try:
        startpart = parts[0]['start_p']
        stoppart = parts[0]['stop_p']
    except:
        startpart = 0
        stoppart = length_sec

    context = {'song_url': urlval, 'startpart': startpart, 'stoppart': stoppart, 'parts': parts, 'lenght_sec': length_sec}
    return render(
        request, template_name='looper.html', context=context)


def looper_with_param(request, song_url, start_p, stop_p):
    song_id = Song.objects.get(song_url=song_url).id
    # part_id = Part.objects.get(song_id=song_id).id

    parts = Part.objects.filter(song_id=song_id).values('start_p', 'stop_p')
    context = {'song_url': song_url, 'startpart': start_p, 'stoppart': stop_p, 'parts': parts}
    return render(
        request, template_name='looper.html', context=context)


