import uuid
from django.utils import timezone

from django.db import models
from django.contrib.auth.models import User


class Publisher(models.Model):
    """出版社モデル"""
    class Meta:
        db_table = 'publisher'
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name='出版社名', max_length=20)
    created_at = models.DateTimeField(default=timezone.now)


class Book(models.Model):
    """本モデル"""
    class Meta:
        db_table = 'book'
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(verbose_name='タイトル',  max_length=20, unique=True)
    price = models.IntegerField(verbose_name='価格', null=True)
    publisher = models.ForeignKey(Publisher, verbose_name='出版社',  on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(default=timezone.now)


class Sample(models.Model):
    name = models.TextField(max_length=1000)


class Message(models.Model):

    # class Meta:
    #     ordering = ('-pub_date',)

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='message_owner')
    group = models.ForeignKey('Group', on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
    shared_id = models.IntegerField(default=-1)
    good_count = models.IntegerField(default=0)
    share_count = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True)


class Group(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='group_owner')
    title = models.CharField(max_length=100)

    # def __str__(self):
    #     return self.title


class Friend(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friend_owner')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)


class Good(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='good_owner')
    message = models.ForeignKey(Message, on_delete=models.CASCADE)




