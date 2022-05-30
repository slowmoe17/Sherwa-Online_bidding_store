from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager
class User(AbstractBaseUser):
    Name = models.CharField(max_length=100)
    Phone = models.CharField(max_length=14 ,unique=True)
    Address = models.TextField()
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "Phone"
    REQUIRED_FIELDS = ["Name","Address"]

    def get_full_name(self):
        # The user is identified by their Names
        return self.Name

    def get_short_name(self):
        "Return the short name for the user."
        return self.Name

    def __str__(self):
        return self.Name + " " + self.Phone

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
