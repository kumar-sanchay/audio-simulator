from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist
from .models import Song, Podcast, ListOfMembers, AudioBooks


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields  = '__all__'


class ListOfMembersSerializer(serializers.ModelSerializer):
    class Meta:

        model = ListOfMembers
        fields = ['member_name']


class PodcastSerializer(serializers.ModelSerializer):

    podcast_members = serializers.SerializerMethodField('get_members')

    class Meta:
        model = Podcast
        fields = ['id', 'name', 'duration', 'uploaded_time', 'host', 'podcast_members']
    
    def get_members(self, obj):

        members = ListOfMembers.objects.filter(podcast=obj)
        members_serialized = ListOfMembersSerializer(members, many=True)
        return members_serialized.data


class AudioBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioBooks
        fields = '__all__'


class SongSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Song
        exclude = ['id']


class AudioBookSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = AudioBooks
        exclude = ['id']


class PodcastSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        exclude = ['id']
