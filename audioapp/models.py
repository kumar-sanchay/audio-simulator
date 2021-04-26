import uuid
from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.core.exceptions import ValidationError


def validate_uploaded_time(date):
    '''
    Validator for datetime
    '''
    if (date + timedelta(minutes=1)) < timezone.now():
        print(date)
        print(timezone.now())
        raise ValidationError('Past Time Not Allowed')


class Audio(models.Model):
    '''
    Abstract Audio Model with common fields
    '''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    uploaded_time = models.DateTimeField(validators=[validate_uploaded_time])

    class Meta:
        abstract = True


class Song(Audio):
    pass


class Podcast(Audio):

    host = models.CharField(max_length=100)


class ListOfMembers(models.Model):
    member_name = models.CharField(max_length=100)
    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        '''
        Checking members not more than 10
        '''
        instance = Podcast.objects.filter(pk=self.podcast.pk)
        if instance.count() <= 10:
            super(ListOfMembers, self).save(*args, **kwargs)
        else:
            raise ValidationError("Number of participants is more than 10.")

class AudioBooks(Audio):

    author = models.CharField(max_length=100)
    narrator = models.CharField(max_length=100)
