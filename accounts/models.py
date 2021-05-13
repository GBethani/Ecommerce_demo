from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
'''
baseusermanager class does NOT have any field names, rather it has two methods. One method is used to create regular users, the other method is used to create superusers. so myaccountmanager class is used to overwrite create_user and create_superuser methods.

AbstractUser is a full User model, complete with fields, as an abstract class so that you can inherit from itand add your own profile fields and methods. AbstractBaseUser only contains the authentication functionality, but no actual fields: you have to supply them when you subclass.

has_perm checks whether the user has a specific permission, for example:
user.has_perm('polls.can_vote')

has_module_perm checks whether the user has any permissions for that app, for example:
user.has_module_perm('polls')
'''
# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self,first_name,last_name,username,email,password=None):
        # check whether email and username are provided
        if not email:
            raise ValueError('User must have an email address')

        if not username:
            raise ValueError('User must have an username')

        # create the user object
        user = self.model(
            first_name = first_name,
            last_name = last_name,
            username = username,
            email = self.normalize_email(email),
        )

        # set password and save to default database
        user.set_password(password)
        user.save(using = self._db)

        return user

    def create_superuser(self,first_name,last_name,username,email,password):
        user = self.create_user(
            first_name = first_name,
            last_name = last_name,
            username = username,
            password = password,
            email = self.normalize_email(email),
        )

        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superadmin = True

        user.save(using = self._db)

        return user
        

class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = PhoneNumberField()

    # required
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']

    def __str__(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True
    