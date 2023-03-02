from django.utils import timezone
from django.test import TestCase
from django.db.utils import IntegrityError

from users.models import User
from users.tests.factories import UserFactory


class TestUsersModels(TestCase):

    def setUp(self):
        self.user = UserFactory.create(first_name='John', last_name='Doe', email='john@gmail.com')

    def test_create_user(self):
        """Test creating of user in database"""

        db_user = User.objects.get(id=self.user.id)

        self.assertEqual(db_user.first_name, 'John')
        self.assertEqual(db_user.last_name, 'Doe')
        self.assertEqual(db_user.email, 'john@gmail.com')
        self.assertEqual(db_user.date_joined.day, timezone.now().day)
        self.assertEqual(db_user.date_joined.month, timezone.now().month)
        self.assertEqual(db_user.date_joined.year, timezone.now().year)

        self.assertEqual(self.user, db_user)

    def test_update_user(self):
        """Test updating created user"""

        self.user.first_name = 'Andrew'
        self.user.last_name = 'Paul'
        self.user.email = 'andrew@gmail.com'
        self.user.save(update_fields=['first_name', 'last_name', 'email'])

        db_user = User.objects.get(id=self.user.id)

        self.assertEqual(db_user.first_name, 'Andrew')
        self.assertEqual(db_user.last_name, 'Paul')
        self.assertEqual(db_user.email, 'andrew@gmail.com')

    def test_delete_user(self):
        """Test deleting created user"""
        self.user.delete()

        with self.assertRaises(User.DoesNotExist):
            User.objects.get(id=self.user.id)

    def test_create_user_with_same_email_unsuccessfully(self):
        """Test create user with same email unsuccessfully"""
        with self.assertRaises(IntegrityError):
            UserFactory.create(email='john@gmail.com')
