from .models import Song, Podcast, AudioBooks, ListOfMembers
from .serializers import SongSerializer, PodcastSerializer, AudioBooksSerializer


def get_song(self, audio_id=None):
    try:

        if audio_id:
            songs = Song.objects.get(id=audio_id)
            serialized_songs = SongSerializer(songs)
        else:
            songs = Song.objects.all()

            serialized_songs = SongSerializer(songs, many=True)

        return serialized_songs

    except ObjectDoesNotExist:
        return None

def get_podcast(self, audio_id=None):

    try:
        if audio_id:
            podcast = Podcast.objects.get(id=audio_id)
            serialized_songs = PodcastSerializer(podcast)
        else:
            podcast = Podcast.objects.all()

            serialized_songs = PodcastSerializer(podcast, many=True)

        return serialized_songs

    except ObjectDoesNotExist:
        return None

def get_audiobook(self, audio_id=None):
    try:
        if audio_id:
            podcast = AudioBooks.objects.get(id=audio_id)
            serialized_songs = AudioBooksSerializer(podcast)
        else:
            podcast = AudioBooks.objects.all()

            serialized_songs = AudioBooksSerializer(podcast, many=True)

        return serialized_songs

    except ObjectDoesNotExist:
        return None