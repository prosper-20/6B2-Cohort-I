from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)
from .managers import UserManager
from django.core.mail import send_mail


class User(AbstractBaseUser, PermissionsMixin):
    """ 
    An abstract base class implementing a fully featured Custom User model with 
    admin-compliant permissions. 

    """
    email = models.EmailField(max_length=40, unique=True)
    username = models.CharField(max_length=25)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self

    def get_full_name(self):
        '''
        Returns the full name of a user which in our case is the email.
        '''
        full_name = '%s' '%s' % (self.first_name) (self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.username

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)
