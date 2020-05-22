from django.urls import path
from . import views

app_name = 'apiv1'

urlpatterns = [
    path('messages/', views.MessageCreateAPIView.as_view()),
    path('groups/', views.GroupCreateAPIView.as_view()),
    path('friends/', views.FriendCreateAPIView.as_view()),
    path('goods/', views.GoodCreateAPIView.as_view()),
    path('samples/', views.SampleCreateAPIView.as_view()),
    # path('books/<pk>/', views.BookUpdateAPIView.as_view()),
]


