#coding: utf-8 
from django.conf import settings
from django.contrib.auth.backends import ModelBackend
from django.core.exceptions import ImproperlyConfigured
from django.db.models import get_model

class CustomUserModelBackend(ModelBackend):
    def authenticate(self, username=None, password=None):
        try:
	    print u"попытка. юзер %s"  % (username)
            user = self.user_class.objects.get(username=username)
      	    print u"пароль %s"  % (password)
      	    print u"encoded %s" % (user.password) 
      	    print u"check is:  %s "  % (user.check_password(password))
            if user.check_password(password):
                return user
        except self.user_class.DoesNotExists:
            return None

    def get_user(self, user_id):
        try:
            return self.user_class.objects.get(pk=user_id)
        except self.user_class.DoesNotExists:
            return None

    @property
    def user_class(self):
        if not hasattr(self, '_user_class'):
            self._user_class = get_model('users','RarogUser')
            if not self._user_class:
                raise ImpropertlyConfigured('Could not get custom user model')
        return self._user_class
