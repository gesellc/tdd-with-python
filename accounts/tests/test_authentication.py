from accounts.authentication import PasswordlessAuthenticationBackend
from django.test import TestCase
from accounts.models import Token, User
from unittest import skip, expectedFailure


class AuthenticationTest(TestCase):
    
    def test_returns_none_if_no_such_token(self):
        result = PasswordlessAuthenticationBackend().authenticate(
            'no-such-token'
        )
        self.assertIsNone(result)
    
    def test_returns_new_user_with_correct_email_if_token_exists(self):
        email ='edith@example.com'
        token = Token.objects.create(email=email)
        user = PasswordlessAuthenticationBackend().authenticate(token.uid)
        new_user = User.objects.get(email=email)
        self.assertEqual(user, new_user)

    def test_returns_existing_user_with_correct_email_if_token_exists(self):
        email ='edith@example.com'
        token = Token.objects.create(email=email)
        existing_user = User.objects.create(email=email)
        user = PasswordlessAuthenticationBackend().authenticate(token.uid)
        self.assertEqual(user, existing_user)

class GetUserTest(TestCase):

    def test_returns_none_if_user_does_not_exist(self):
        user = PasswordlessAuthenticationBackend().get_user('no-such-email')
        self.assertIsNone(user)

    def test_gets_user_by_email(self):
        email ='edith@example.com'
        desired_user = User.objects.create(email=email)
        User.objects.create(email='another@example.com')

        user = PasswordlessAuthenticationBackend().get_user(email)
        
        self.assertEqual(user, desired_user)
        