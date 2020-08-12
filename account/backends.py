from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

from account.models import UserProfile

class EmailBackend(ModelBackend):

    def authenticate(self, request, **kwargs):
        email = kwargs['username']
        password = kwargs['password']
        try:
            customer = User.objects.get(email= email)
            if customer.check_password(password) is True:
                return customer
        except User.DoesNotExist:
            pass