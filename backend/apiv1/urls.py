from django.urls import include, path

from . import views


app_name = 'apiv1'

urlpatterns = [





    path('register/', views.UserRegisterAPIView.as_view()),

    path('messages/', views.MessageListAPIView.as_view()),
    path('messages/create/', views.MessageCreateAPIView.as_view()),
    path('messages/<pk>/', views.MessageRetrieveUpdateDestroyAPIView.as_view()),
    path('groups/', views.GroupListAPIView.as_view()),
    path('groups/create/', views.GroupCreateAPIView.as_view()),
    path('groups/<pk>/', views.GroupRetrieveUpdateDestroyAPIView.as_view()),
    path('friends/', views.FriendListAPIView.as_view()),
    path('friends/create/', views.FriendCreateAPIView.as_view()),
    path('friends/<pk>/', views.FriendRetrieveUpdateDestroyAPIView.as_view()),
    path('goods/', views.GoodListAPIView.as_view()),
    path('goods/create/', views.GoodCreateAPIView.as_view()),
    path('goods/<pk>/', views.GoodRetrieveUpdateDestroyAPIView.as_view()),

    


    # path('books/<pk>/', views.BookUpdateAPIView.as_view()),
]


