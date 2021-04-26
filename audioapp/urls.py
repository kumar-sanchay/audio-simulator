from django.urls import path
from .api import AudioFileAPI, CreateAudioAPI, UDOperation

app_name = 'audioapp'

urlpatterns = [
    path('get-audio/<str:audio_type>/', AudioFileAPI.as_view()),
    path('get-audio/<str:audio_type>/<uuid:audio_id>/', AudioFileAPI.as_view()),

    path('create-audio/', CreateAudioAPI.as_view()),
    path('audio-operation/<str:audio_type>/<uuid:audio_id>/', UDOperation.as_view()),
]