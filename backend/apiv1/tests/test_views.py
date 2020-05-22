from django.utils.timezone import localtime
from rest_framework.test import APITestCase

from django.contrib.auth.models import User
from apiv1.models import Sample, Message, Group, Friend, Good


class TestMessageCreateAPIView(APITestCase):

    TARGET_URL = '/api/v1/messages/'

    def setUp(self):
        print("# {} is running!".format(self.id()))
        self.user = User.objects.create_user(username='lauren', password='12345678')
        self.group = Group.objects.create(owner=self.user, title='title')


    def test_create_success(self):

        time = str(localtime())

        params = {
            'owner': self.user.pk,
            'group': self.group.pk,
            'content': 'content',
            'shared_id': 1,
            'good_count': 1,
            'share_count': 1,
            'pub_date': localtime(),
        }

        response = self.client.post(self.TARGET_URL, params, format='json')

        self.assertEqual(Message.objects.count(), 1)
        self.assertEqual(response.status_code, 201)

        message = Message.objects.get()

        expected_json_dict = {
            'id': message.id,
            'owner': message.owner.pk,
            'group': message.group.pk,
            'content': message.content,
            'shared_id': message.shared_id,
            'good_count': message.good_count,
            'share_count': message.share_count,
            'pub_date': str(localtime(message.pub_date)).replace(' ', 'T'),
        }

        self.assertJSONEqual(response.content, expected_json_dict)


class TestGroupCreateAPIView(APITestCase):

    TARGET_URL = '/api/v1/groups/'

    def setUp(self):
        print("# {} is running!".format(self.id()))
        self.user = User.objects.create_user(username='lauren', password='12345678')

    def test_create_success(self):

        params = {
            'owner': self.user.pk,
            'title': 'title',
        }

        response = self.client.post(self.TARGET_URL, params, format='json')

        self.assertEqual(Group.objects.count(), 1)
        self.assertEqual(response.status_code, 201)

        group = Group.objects.get()
        expected_json_dict = {
            'id': group.id,
            'owner': group.owner.pk,
            'title': group.title,
        }

        self.assertJSONEqual(response.content, expected_json_dict)


class TestFriendCreateAPIView(APITestCase):

    TARGET_URL = '/api/v1/friends/'

    def setUp(self):
        print("# {} is running!".format(self.id()))
        self.user = User.objects.create_user(username='lauren', password='12345678')
        self.group = Group.objects.create(owner=self.user, title='title')

    def test_create_success(self):

        params = {
            'owner': self.user.pk,
            'user': self.user.pk,
            'group': self.group.pk,
        }

        response = self.client.post(self.TARGET_URL, params, format='json')

        self.assertEqual(Friend.objects.count(), 1)
        self.assertEqual(response.status_code, 201)

        friend = Friend.objects.get()
        expected_json_dict = {
            'id': friend.id,
            'owner':friend.owner.pk,
            'user': friend.user.pk,
            'group': friend.group.pk,
        }

        self.assertJSONEqual(response.content, expected_json_dict)


class TestGoodCreateAPIView(APITestCase):

    TARGET_URL = '/api/v1/goods/'

    def setUp(self):
        print("# {} is running!".format(self.id()))
        self.user = User.objects.create_user(username='lauren', password='12345678')
        self.group = Group.objects.create(owner=self.user, title='title')
        self.message = Message.objects.create(
            owner=self.user,
            group=self.group,
            content='content',
            shared_id=1,
            good_count=1,
            share_count=1,
            pub_date=str(localtime()),
        )

    def test_create_success(self):

        params = {
            'owner': self.user.pk,
            'message': self.message.pk,
        }

        response = self.client.post(self.TARGET_URL, params, format='json')

        self.assertEqual(Good.objects.count(), 1)
        self.assertEqual(response.status_code, 201)

        good = Good.objects.get()
        expected_json_dict = {
            'id': good.id,
            'owner': good.owner.pk,
            'message': good.message.pk,
        }

        self.assertJSONEqual(response.content, expected_json_dict)


















# class TestMessageCreateAPIView(APITestCase):

#     TARGET_URL = '/api/v1/messsages/'

#     def test_create_success(self):

#         params = {
#             'owner': 'aaa'
#         }

#         response = self.client.post(self.TARGET_URL, params, format='json')

#         self.assertEqual(Message.objects.count(), 1)


    # def 作成に成功した(APITestCase):
        
    #     params = {
    #         'owner': 'aaa'
    #     }

    #     response = self.client.post(self.TARGET_URL, params, format='json')

    #     self.assertEqual(Message.objects.count(), 0)
