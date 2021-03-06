from django.db import models
from .managers import UserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

# Create your models here.
class User(AbstractBaseUser,PermissionsMixin):
    mobile_number = models.CharField(max_length=10,unique=True,null=False,blank=False)
    first_name = models.CharField(max_length=20,null=False,blank=False)
    last_name = models.CharField(max_length=20,null=False,blank=False)
    email = models.EmailField(blank=False,null=False,unique=True)
    password = models.CharField(max_length=200,null=False,blank=False)
    confirm_password = models.CharField(max_length=200,null=False,blank=False)
    new_user = models.BooleanField(default=True)
    otp_send = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    def make_exist_user(self):
        self.new_user = False
        self.save()

    def make_otp_send(self):
        self.otp_send = True
        self.save()

    USERNAME_FIELD = 'mobile_number'
    REQUIRED_FIELDS = []
    objects = UserManager()
    

    def __str__(self):
        full_name = self.first_name+ ' ' + self.last_name
        return self.mobile_number
