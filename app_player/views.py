from logging import getLogger
from django.shortcuts import render
# from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView
from app_player.models import Song, Part
from app_player.forms import SongForm, PartForm
from django.views.generic.detail import SingleObjectMixin

LOGGER = getLogger()


class PlayerView(ListView):
    template_name = 'songs.html'
    model = Song


class SongCreateView(CreateView):
    template_name = 'form.html'
    form_class = SongForm
    success_url = reverse_lazy('add_song')

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data.')
        return super().form_invalid(form)


class SongUpdateView(UpdateView):
    template_name = 'form.html'
    model = Song
    form_class = SongForm


class LooperUpdateView(UpdateView):
    template_name = 'looper_update.html'
    model = Part
    form_class = PartForm



def looper(request, pk):
    urlval = Song.objects.get(id=pk).song_url
    parts = Part.objects.filter(song_id=pk).values('start_p', 'stop_p')
    try:
        startpart = parts[0]['start_p']
        stoppart = parts[0]['stop_p']
    except:
        startpart = 0
        stoppart = 0
    context = {'song_url': urlval, 'startpart': startpart, 'stoppart': stoppart, 'parts': parts}
    return render(
        request, template_name='looper.html', context=context)


def looper_with_param(request, song_url, start_p, stop_p):
    song_id = Song.objects.get(song_url=song_url).id
    # part_id = Part.objects.get(song_id=song_id).id

    parts = Part.objects.filter(song_id=song_id).values('start_p', 'stop_p')
    context = {'song_url': song_url, 'startpart': start_p, 'stoppart': stop_p, 'parts': parts}
    return render(
        request, template_name='looper.html', context=context)
