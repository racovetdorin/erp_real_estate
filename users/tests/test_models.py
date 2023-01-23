from django.utils import timezone
from django.test import TestCase

from users.models import User
from users.tests.factories import UserFactory


class TestUsersModels(TestCase):

    def setUp(self):
        self.user = UserFactory.create(first_name='John', last_name='Doe', email='andrew@gmail.com')

    def test_create_user(self):
        """Test creating of user in database"""

        self.assertEqual(self.user.first_name, 'John')
        self.assertEqual(self.user.last_name, 'Doe')
        self.assertEqual(self.user.email, 'andrew@gmail.com')
        self.assertEqual(self.user.date_joined.day, timezone.now().day)
        self.assertEqual(self.user.date_joined.month, timezone.now().month)
        self.assertEqual(self.user.date_joined.year, timezone.now().year)

        db_user = User.objects.get(id=self.user.id)

        self.assertEqual(self.user, db_user)

    def test_update_user(self):
        """Test updating created user"""
        pass
