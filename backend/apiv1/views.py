from rest_framework import generics
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.permissions import IsAuthenticated

from .models import Sample, Message, Group, Friend, Good
from .serializers import SampleSerializer, MessageSerializer, GroupSerializer, FriendSerializer, GoodSerializer


class SampleCreateAPIView(generics.CreateAPIView):

    queryset = Sample.objects.all()
    serializer_class = SampleSerializer


class MessageCreateAPIView(generics.CreateAPIView):

    queryset = Message.objects.all()
    serializer_class = MessageSerializer



class GroupCreateAPIView(generics.CreateAPIView):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FriendCreateAPIView(generics.CreateAPIView):

    queryset = Friend.objects.all()
    serializer_class = FriendSerializer


class GoodCreateAPIView(generics.CreateAPIView):

    queryset = Good.objects.all()
    serializer_class = GoodSerializer






#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


# class BookUpdateAPIView(generics.UpdateAPIView):

#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     authentication_classes = [SessionAuthentication]
#     permission_classes = [IsAuthenticated]

