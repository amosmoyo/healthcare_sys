from django.contrib.auth import validators
from django.utils.http import parse_http_date_safe
from rest_framework.test import APITestCase
from authetifications.models import User


class Testmodels(APITestCase):
  
  def test_create_user(self):
    # self.assertEqual(1, 1-0)
    user = User.objects.create_user('amos', 'amos@gmail.com', '1111')
    # testing
    self.assertIsInstance(user, User)
    self.assertFalse(user.is_staff)
    self.assertEqual(user.email, 'amos@gmail.com')

  # test for username
  def test_raises_error_when_username(self):
    # run this test to validate

    #self.assertRaises(ValueError, User.objects.create_user, email='amos@gmail.com', password='1111')

    # second test with name
    self.assertRaises(ValueError, User.objects.create_user, username='', email='amos@gmail.com', password='1111')
  
  # test for email
  def test_raises_error_with_message_when_no_email(self):
    with self.assertRaisesMessage(ValueError,'The given email must be set'):
      User.objects.create_user(username='amos', email='', password='1111')
       # user = User.objects.create_user(name='amos', email='amos@gmail.com', password='1111')

  def test_create_superuser(self):
    # self.assertEqual(1, 1-0)
    user = User.objects.create_superuser('amos', 'amos@gmail.com', '1111')
    # testing
    self.assertIsInstance(user, User)
    self.assertTrue(user.is_staff)
    self.assertEqual(user.email, 'amos@gmail.com')

  # test if superuser is staff
  def test_raises_error_with_message_when_superuser_is_staff(self):
    with self.assertRaisesMessage(ValueError,'Superuser must have is_staff=True.'):
      User.objects.create_superuser(username='amos', email='', password='1111', is_staff=False)

  # test if superuser is is superuser
  def test_raises_error_with_message_when_superuser_is_superuser(self):
    with self.assertRaisesMessage(ValueError,'Superuser must have is_superuser=True.'):
      User.objects.create_superuser(username='amos', email='', password='1111', is_superuser=False)

