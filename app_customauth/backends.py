from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password

from app_customauth.models import CustomUser


class SettingsBackend(BaseBackend):

    """
    Authenticate against the settings ADMIN_LOGIN and ADMIN_PASSWORD.

    """

    
    def authenticate(self, request, login=None, password=None):

        #import pdb; pdb.set_trace()
        # get the user
        user = CustomUser.objects.filter(login=login).first()

        if user:
            pwd_valid = check_password(password=password, encoded=user.password)

            if pwd_valid:
                return user
        return None
    
    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None
