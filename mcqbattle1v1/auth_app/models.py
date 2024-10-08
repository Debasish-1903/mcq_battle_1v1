from django.db import models
from django.contrib.auth.models import AbstractBaseUser ,BaseUserManager ,PermissionsMixin
from django.utils.translation import gettext as _
from django.utils import timezone

# Create your models here.


class UserManager(BaseUserManager):

    def create_user(self,email,password=None,**extra_fields):

        if not email:
            raise ValueError("The email field must be set")
        
        email=self.normalize_email(email)
        user=self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,password,**extra_fields):

        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',True)

      
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)
          



class User(AbstractBaseUser):    
    first_name = models.CharField( max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
      

    objects=UserManager()


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return True
