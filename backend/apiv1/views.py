from rest_framework import generics





# from rest_framework.authentication import SessionAuthentication
# from rest_framework.permissions import IsAuthenticated

from .models import Sample, Message, Group, Friend, Good
from django.contrib.auth.models import User

from .serializers import UserSerializer, MessageSerializer, GroupSerializer, FriendSerializer, GoodSerializer


class UserRegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MessageListAPIView(generics.ListAPIView):

    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageCreateAPIView(generics.CreateAPIView):

    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class GroupListAPIView(generics.ListAPIView):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupCreateAPIView(generics.CreateAPIView):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FriendListAPIView(generics.ListAPIView):

    queryset = Friend.objects.all()
    serializer_class = FriendSerializer


class FriendCreateAPIView(generics.CreateAPIView):

    queryset = Friend.objects.all()
    serializer_class = FriendSerializer


class FriendRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Friend.objects.all()
    serializer_class = FriendSerializer


class GoodListAPIView(generics.ListAPIView):

    queryset = Good.objects.all()
    serializer_class = GoodSerializer


class GoodCreateAPIView(generics.CreateAPIView):

    queryset = Good.objects.all()
    serializer_class = GoodSerializer


class GoodRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Good.objects.all()
    serializer_class = GoodSerializer


#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


# class BookUpdateAPIView(generics.UpdateAPIView):

#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     authentication_classes = [SessionAuthentication]
#     permission_classes = [IsAuthenticated]

