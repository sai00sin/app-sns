from django.utils.timezone import localtime
from django.test import TestCase

from django.contrib.auth.models import User
from apiv1.models import Message, Group, Friend, Good
from apiv1.serializers import MessageSerializer, GroupSerializer, FriendSerializer, GoodSerializer



class TestMessageSerializer(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='lauren', password='12345678')
        self.group = Group.objects.create(owner=self.user, title='title')

    def test_input_valid(self):

        input_data = {
            'owner': self.user.pk,
            'group': self.group.pk,
            'content': 'content',
            'shared_id': 1,
            'good_count': 1,
            'share_count': 1,
            'pub_date': localtime(),
        }
        serializer = MessageSerializer(data=input_data)

        self.assertEqual(serializer.is_valid(), True)

    def test_output_data(self):

        message = Message.objects.create(
            owner=self.user,
            group=self.group,
            content='content',
            shared_id=1,
            good_count=1,
            share_count=1,
            pub_date=localtime(),
        )
        serializer = MessageSerializer(instance=message)

        expected_data = {
            'id': message.id,
            'owner': message.owner.pk,
            'group': message.group.pk,
            'content': message.content,
            'shared_id': message.shared_id,
            'good_count': message.good_count,
            'share_count': message.share_count,
            'pub_date': str(localtime(message.pub_date)).replace(' ', 'T'),
        }
        self.assertDictEqual(serializer.data, expected_data)


class TestGroupSerializer(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='lauren', password='12345678')

    def test_input_valid(self):

        input_data = {
            'owner': self.user.pk,
            'title': 'title',
        }
        serializer = GroupSerializer(data=input_data)

        self.assertEqual(serializer.is_valid(), True)

    def test_input_invalid_if_title_is_blank(self):

        input_data = {
            'owner': self.user.pk,
            'title': '',
        }
        serializer = GroupSerializer(data=input_data)

        self.assertEqual(serializer.is_valid(), False)

        self.assertCountEqual(serializer.errors.keys(), ['title'])
        self.assertCountEqual(
            [x.code for x in serializer.errors['title']],
            ['blank']
        )

    def test_output_data(self):

        group = Group.objects.create(
            owner=self.user,
            title='title',
        )
        serializer = GroupSerializer(instance=group)

        expected_data = {
            'id': group.id,
            'owner': group.owner.pk,
            'title': group.title,
        }
        self.assertDictEqual(serializer.data, expected_data)


class TestFriendSerializer(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='lauren', password='12345678')
        self.group = Group.objects.create(owner=self.user, title='title')

    def test_input_valid(self):

        input_data = {
            'owner': self.user.pk,
            'user':  self.user.pk,
            'group': self.group.pk,
        }
        serializer = FriendSerializer(data=input_data)

        self.assertEqual(serializer.is_valid(), True)

    def test_output_data(self):

        group = Group.objects.create(
            owner=self.user,
            title='title',
        )
        serializer = GroupSerializer(instance=group)

        expected_data = {
            'id': group.id,
            'owner': group.owner.pk,
            'title': group.title,
        }
        self.assertDictEqual(serializer.data, expected_data)


class TestGoodSerializer(TestCase):

    def setUp(self):
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

    def test_input_valid(self):

        input_data = {
            'owner': self.user.pk,
            'message': self.message.pk,
        }
        serializer = GoodSerializer(data=input_data)

        self.assertEqual(serializer.is_valid(), True)

    def test_output_data(self):

        good = Good.objects.create(
            owner=self.user,
            message=self.message,
        )
        serializer = GoodSerializer(instance=good)

        expected_data = {
            'id': good.id,
            'owner': good.owner.pk,
            'message': good.message.pk,
        }
        self.assertDictEqual(serializer.data, expected_data)









'''
from django.utils.timezone import localtime
from django.test import TestCase

from apiv1.models import Book
from apiv1.serializers import BookSerializer


class TestBookSerializer(TestCase):

    def test_input_valid(self):
        input_data = {
            'title': 'aaa',
        }
        serializer = BookSerializer(data=input_data)
        self.assertEqual(serializer.is_valid(), True)

    def test_input_invalid_if_title_is_blank(self):
        input_data = {
            'title': '',
        }
        serializer = BookSerializer(data=input_data)

        self.assertEqual(serializer.is_valid(), False)

        self.assertCountEqual(serializer.errors.keys(), ['title'])

        self.assertCountEqual(
            [x.code for x in serializer.errors['title']],
            ['blank'],
        )

    def test_output_data(self):

        book = Book.objects.create(
            title='aaa',
        )
        serializer = BookSerializer(instance=book)

        expected_data = {
            'id': str(book.id),
            'title': book.title,
            'created_at': str(localtime(book.created_at)).replace(' ', 'T'),
        }
        self.assertEqual(serializer.data, expected_data)

'''