from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, Group


# Create your models here.
GENDER_CHOICE = (
    (0, 'Female'),
    (1, 'Male'),
    (2, 'Not to disclose'),
)


class UserManager(BaseUserManager):

    def _create_user(self, email, username, password, gender=2, **extra_fields):

        """

        Create and save a user with the given username, email, and password.

        """

        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)

        username = self.model.normalize_username(username)

        user = self.model(email=email, username=username, gender=gender, **extra_fields)

        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_user(self, email, username='', password=None, **extra_fields):

        extra_fields.setdefault('is_staff', False)

        extra_fields.setdefault('is_superuser', False)

        return self._create_user(email, username, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):

        extra_fields.setdefault('is_staff', True)

        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, 'blogs/like_section.html', password, **extra_fields)


class User(AbstractUser):
    gender = models.SmallIntegerField(choices=GENDER_CHOICE)
    birth_date = models.DateField(null=True, blank=True)
    org_domain = models.TextField(max_length=50)
    
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    username = models.CharField(max_length=30)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    # 필수로 받고 싶은 필드들 넣기 
    # 원래 소스 코드엔 email필드가 들어가지만 
    # 우리는 로그인을 이메일로 하니깐..
    REQUIRED_FIELDS = []  

    def __str__(self):
        # return "<%d %s>" % (self.pk, self.email)
        return " %s (%s) " % (self.first_name, self.org_domain)


# Extend Group
class StaffGroup(Group):
    notes = models.TextField(max_length=255, blank=True)

    objects = models.Manager()

    class Meta:
        verbose_name_plural = "Staffs Group"
        ordering = ['name']

    def __str__(self) -> str:
        return self.name
    




