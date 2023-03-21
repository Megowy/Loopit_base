from django.db.models import Model, CharField, URLField, TextField, ForeignKey, CASCADE, IntegerField
from django.urls import reverse


class Song(Model):
    # user = ForeignKey(User, )
    band = CharField(max_length=30, null=False)
    song_title = CharField(max_length=30, null=False)
    song_url = CharField(max_length=15, null=False)
    description = TextField(blank=True, null=True)

    def __str__(self):
        return str(self.band) if self.band else " No such a song "

    def get_absolute_url(self):
        return reverse('index')


class Part(Model):
    song = ForeignKey(Song, on_delete=CASCADE)
    start_p = IntegerField()
    stop_p = IntegerField()
    dedescription_p = TextField(blank=True, null=True)

    def __str__(self):
        return str(self.song) if self.song else " Brak "

# class  YoutubeGet(Model):
#     objects = None
#     y_title = CharField(max_length=200)
#     y_body = TextField()
#     y_video = EmbedVideoField()
#
#     class Meta:
#         verbose_name_plural = "Youtube"
#
#     def  __str__(self):
#         return  str(self.y_title) if  self.y_title  else  " "
#
