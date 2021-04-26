from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ListOfMembers, Song, Podcast, AudioBooks
from django.core.exceptions import ObjectDoesNotExist
from .events import get_song, get_podcast, get_audiobook
from .serializers import SongSerializerCreate, AudioBookSerializerCreate, PodcastSerializerCreate


class AudioFileAPI(APIView):

    '''
    Get api for audio files according to audiotype and audio_id if exists
    '''
    def get(self, request, audio_type, audio_id=None):
        
        response = None

        if audio_type == 'song':
            response = get_song(audio_id)
        
        elif audio_type == 'podcast':
            response = get_podcast(audio_id)

        elif audio_type == 'audiobook':
            response = get_audiobook(audio_id)

        return Response({"data": response.data}, status=status.HTTP_200_OK)


class CreateAudioAPI(APIView):

    '''
    Audio file create api

    Request Body:

    For audiotype = song
    {
        "audiotype": "song",
        "name": <name_of_file>,
        "duration": <in_sec>,
        "uploaded_time": <current date time>
    }

    For audiotype = podcast

    {
        "audiotype": "podcast",
        "name": <name>,
        "duration":<duration>,
        "uploaded_time": "<uploaded_time>",

        "host":<host>,

        "members": ["MEM1", "MEM2"]
    }

    For audiotype = audiobook
    {
        "audiotype": "audiobook",
        "name": <name_of_file>,
        "duration": <in_sec>,
        "uploaded_time": <current date time>,
        "author": <author name>,
        "narrator": <narrator name>
    }
    '''
    def post(self, request):

        data = request.data

        if 'audiotype' not in data:
            return Response({'data': 'audiotype field does not exists'}, status=status.HTTP_400_BAD_REQUEST)


        if data['audiotype'] == 'song':
            del data['audiotype']
            song = SongSerializerCreate(data=data)
            song.is_valid(raise_exception=True)
            song.save()
        
        elif data['audiotype'] == 'audiobook':
            del data['audiotype']
            audiobook = AudioBookSerializerCreate(data=data)
            audiobook.is_valid(raise_exception=True)
            audiobook.save()
        
        elif data['audiotype'] == 'podcast':

            initial = data

            del data['audiotype']
            del data['members']

            podcast = PodcastSerializerCreate(data=data)
            podcast.is_valid(raise_exception=True)
            podcast = podcast.save()

            if 'members' in initial:
                ListOfMembers.objects.bulk_create(
                    [ListOfMembers(member_name=i, podcast=podcast) for i in members_list]
                )

        else:
            return Response({'data': 'Enter Valid audiotype'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'data': 'Object Created Successfully'})


class UDOperation(APIView):
    '''
    Performing update and delete operation based on audiotype and audio_id

    UPDATE Request

    Request Body example:
    {

        "name": "updated-name"
    }
    '''
    def put(self, request, audio_type, audio_id):
        
        err = False
        if audio_type == 'song':
            try:
                song = Song.objects.get(pk=audio_id)
                
                for key, val in request.data.items():
                    setattr(song, key, val)
                song.save()
            except Exception as e:
                print(e)
                err = True
        
        elif audio_type == 'audiobook':
            try:
                audiobook = AudioBooks.objects.get(pk=audio_id)
                for key, val in request.data.items():
                    setattr(audiobook, key, val)
                audiobook.save()
            except Exception as e:
                print(e)
                err = True

        elif audio_type == 'podcast':
            try:
                podcast = Podcast.objects.get(pk=audio_id)
                for key, val in request.data.items():
                    setattr(podcast, key, val)
                podcast.save()
            except Exception as e:
                print(e)
        
        else:
            err = True
        
        if err:
            return Response({'data': 'Something Went Wrong!'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'data': 'Object updated Successfully'})


    def delete(self, request, audio_type, audio_id):

        err = False
        if audio_type == 'song':
            
            try:
                Song.objects.filter(id=audio_id).delete()
            except ObjectDoesNotExist:
                err = True
        
        elif audio_type == 'audiobook':
            try:
                AudioBooks.objects.filter(id=audio_id).delete()
            except ObjectDoesNotExist:
                err = True
        
        elif audio_type == 'podcast':
            try:
                Podcast.objects.filter(id=audio_id).delete()
            except ObjectDoesNotExist:
                err = True
        
        else:
            err = True
        
        if err:
            return Response({'data': 'Something Went Wrong!'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'data': 'Object Deleted'})