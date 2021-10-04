from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)

from django.utils import timezone

# from healpers.models import TrackModel
# from django.contrib.auth.validators import UnicodeUsernameValidator
# from django.utils.translation import gettext_lazy as _ 
# from django.utils import timezone
# from django.apps import apps
# from django.contrib.auth.hashers import make_password

# import jwt
# from django.conf import settings

# from datetime import datetime, timedelta

# Create your models here.
"""class MyUserManager(UserManager):
  def _create_user(self, username, email, password, **extra_fields):
          
          #Create and save a user with the given username, email, and password.
          
          if not username:
              raise ValueError('The given username must be set')

          if not email:
              raise ValueError('The given email must be set')

          email = self.normalize_email(email)
          # Lookup the real model class from the global app registry so this
          # manager method can be used in migrations. This is fine because
          # managers are by definition working on the real model.
          GlobalUserModel = apps.get_model(
              self.model._meta.app_label, self.model._meta.object_name)
          username = GlobalUserModel.normalize_username(username)
          user = self.model(username=username, email=email, **extra_fields)
          user.password = make_password(password)
          user.save(using=self._db)
          return user

  def create_user(self, username, email, password=None, **extra_fields):
          extra_fields.setdefault('is_staff', False)
          extra_fields.setdefault('is_superuser', False)
          return self._create_user(username, email, password, **extra_fields)

  def create_superuser(self, username, email, password=None, **extra_fields):
          extra_fields.setdefault('is_staff', True)
          extra_fields.setdefault('is_superuser', True)

          if extra_fields.get('is_staff') is not True:
              raise ValueError('Superuser must have is_staff=True.')
          if extra_fields.get('is_superuser') is not True:
              raise ValueError('Superuser must have is_superuser=True.')

          return self._create_user(username, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin, TrackModel):
  username_validator = UnicodeUsernameValidator()

  username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
  first_name = models.CharField(_('first name'), max_length=150, blank=True)
  last_name = models.CharField(_('last name'), max_length=150, blank=True)
  email = models.EmailField(_('email address'), blank=False, unique=True)
  is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
  is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
  date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
  email_verified = models.BooleanField(
        _('email_verified'),
        default=False,
        help_text=_(
            'Designates whether this user email should be verified'
        ),
    )
  
  objects = MyUserManager()

  EMAIL_FIELD = 'email'
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username']
  
  @property
  def token(self):
    token = jwt.encode({'username':self.username, 'email':self.email, 'exp':datetime.utcnow() + timedelta(hours=24)}, settings.SECRET_KEY, algorithm='HS256')

    return token
"""
class UserManager(BaseUserManager):
    def create_user(self, username, email, is_staff, is_superuser, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        now = timezone.now()  
        user = self.model(
            email=self.normalize_email(email),
            is_staff=is_staff, 
            is_active=True,
            is_superuser=is_superuser, 
            last_login=now,
            date_joined=now, 

            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password, **extra_fields):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password,
            False, 
            False,
            
            **extra_fields
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password,

            False,

            False,

            **extra_fields
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

# hook in the New Manager to our Model
class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    name = models.CharField(max_length=254, null=True, blank=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True, null=True)

    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser

    # notice the absence of a "Password field", that is built in.

    oobjects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password'] # Email & Password are required by default.

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin
