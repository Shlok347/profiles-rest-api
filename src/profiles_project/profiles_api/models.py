from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserProfileManager(BaseUserManager):

    def create_user(self, email, name, password= None):
        if not email:
            raise ValueError('User must have email address')

        email=self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self,email,username, password):
        user= self.create_user(email,name, password)

        user.is_superuser=True
        user.is_staff = True

        user.save(using=self.db)
        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    user_id = models.CharField(max_length=64, unique=True)
    name = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    imei = models.CharField(max_length=64, unique=True)
    lock_password = models.CharField(max_length=32)
    master_id = models.CharField(max_length=64)
    master_password = models.CharField(max_length=32)

    objects = UserProfileManager()
    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.user_id
