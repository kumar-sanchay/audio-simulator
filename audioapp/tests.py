from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.utils import timezone
from .models import Song, AudioBooks


class GetAudioFileTest(APITestCase):
    '''
    UNIT TESTING Module
    '''
    def setUp(self):

        self.song_obj = Song.objects.create(
            name="MySongExample",
            duration=122,
            uploaded_time="2021-04-26T18:28:50Z"
        )

        self.audio_book_obj = AudioBooks.objects.create(
            name="MySongExample",
            duration=122,
            uploaded_time="2021-04-26T18:28:50Z",
            author='ABC',
            narrator='XYZ'
        )

    def test_post_full_audio_test(self):

        data = {
                "audiotype": "podcast",
                "name": "MyPodcast2",
                "duration":100,
                "uploaded_time": "2021-04-26T18:28:50Z",
                "host":"Sanchay",
                "members": ["MEM1", "MEM2"]
                }

        data1 = {
                "audiotype": "song",
                "name": "Mysong",
                "duration":111,
                "uploaded_time": "2021-04-26T18:28:50Z"
                }
        
        response = self.client.post('/api/create-audio/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.post('/api/create-audio/', data1, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    

    def test_update_request(self):

        data1 = {
            'name': 'Update-name'
        }

        data2 = {
            'name': 'Update-name',
            'duration': 12
        }


        response = self.client.put(f'/api/audio-operation/song/{self.song_obj.pk}/', data1, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)


        response = self.client.put(f'/api/audio-operation/song/{self.song_obj.pk}/', data2, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
    

    def test_delete(self):

        response = self.client.delete(f'/api/audio-operation/song/{self.song_obj.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        response = self.client.delete(f'/api/audio-operation/song/{self.audio_book_obj.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)