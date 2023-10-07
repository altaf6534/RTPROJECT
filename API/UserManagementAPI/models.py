from django.db import models
# from django.contrib.auth.models import User

from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
import uuid, math, random

# UserModel = get_user_model()
# Create your models here.
USER_TYPE_CHOICES = [
    ('', ''),
    ('admin', 'admin'),
    ('merchant', 'merchant'),
    ('plumber', 'plumber'),
]

class UserType(models.Model):
     """user types choices - admin, merchant, plumber"""
     user_type_id = models.AutoField(primary_key=True)
     user_type = models.CharField(max_length=255, choices=USER_TYPE_CHOICES)

     
class UserManager(BaseUserManager):
# 
    def create_user(self, mobile, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not mobile:
            raise ValueError('Users must have an mobile number')
        user = self.model( mobile = mobile, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, mobile, password):
        """Creates and saves a new super user"""
        user = self.create_user(mobile, password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)

        return user
    
class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using mobile instead of username"""
    pkid = models.BigAutoField(primary_key=True)
    user_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_type = models.ForeignKey(UserType,  on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    profile_photo = models.ImageField(upload_to="profile picture", blank=False, null=False)
    email = models.EmailField(max_length=255, unique=True)
    country_code = models.CharField(max_length=7)
    mobile = models.CharField(max_length=20, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    
    USERNAME_FIELD = 'mobile'     

class OTP(models.Model):
    pkid = models.BigAutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    email_otp = models.CharField(max_length=6, blank=True, null=True)
    is_email_verified = models.BooleanField(default=False)
    # country_code = models.CharField(max_length=7)
    # mobile = models.CharField(max_length=20)
    # full_mobile = models.CharField(max_length=20)
    # mobile_otp = models.CharField(max_length=6, blank=True, null=True)
    # is_mobile_verified = models.BooleanField(default=False)

    
    def GenerateOPT():
        corpus= "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        generate_OTP = "" 
        size=6
        length = len(corpus) 
        for i in range(size) : 
            generate_OTP+= corpus[math.floor(random.random() * length)]
        return generate_OTP



