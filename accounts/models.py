from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

class AccountUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('Email is Required')
        
        if not username:
            raise ValueError('Username is Required')
        
        user = self.model (
            email = self.normalize_email(email).lower(),
            username = username,
        )

        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self,username, email, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_admin=True
        user.is_staff=True
        user.is_active=True
        user.is_superadmin=True
        user.role = 'admin'
        user.save(using=self._db)
        return user
    
class Accounts(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=False)
    email = models.EmailField(max_length=100, unique=True)
    role = models.CharField(max_length=20, default='patient')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = AccountUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True
    
    class Meta:
        verbose_name_plural = "USER ACCOUNTS"