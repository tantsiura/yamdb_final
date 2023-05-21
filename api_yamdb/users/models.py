from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.db.models import Q

USER = 'user'
MODERATOR = 'moderator'
ADMIN = 'admin'
ROLES = [
    (USER, 'user'),
    (ADMIN, 'admin'),
    (MODERATOR, 'moderator')
]


class User(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=True,
        validators=[RegexValidator(
            regex=r'^[\w.@+-]+\z$',)
        ]
    )
    email = models.EmailField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    bio = models.TextField(blank=True)
    role = models.CharField(
        choices=ROLES,
        default=USER,
        max_length=150
    )

    def is_moderator(self):
        return self.role == self.MODERATOR

    def is_admin(self):
        return self.role == self.ADMIN

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=Q(username__iexact='me'),
                name='username_not_me'
            )
        ]
