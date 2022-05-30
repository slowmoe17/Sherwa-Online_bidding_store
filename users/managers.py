from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self ,Name, Phone, Address, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not Phone:
            raise ValueError("Users must Phone")

        user = self.model(
             Name=Name, Address = Address, Phone=Phone,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, Name, Phone, Address, password):
        """Create and save a new superuser with given details"""

        user = self.create_user(Name,Phone, Address, password)

        user.admin = True
        user.staff = True

        user.save(using=self._db)
        return user