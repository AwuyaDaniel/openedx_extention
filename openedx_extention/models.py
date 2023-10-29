"""
Database models for IBL_openedx_app.
"""
# from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid


class Greeting(models.Model):
    """
    Greeting: Save greeting from users.

    information, see OEP-30:
    https://open-edx-proposals.readthedocs.io/en/latest/oep-0030-arch-pii-markup-and-auditing.html
    """
    name = models.CharField(max_length=250, default=uuid.uuid4, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    greeting = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        # Update the "updated_on" field before saving
        self.updated_on = timezone.now()
        super().save(*args, **kwargs)

    # TODO: add field definitions

    def __str__(self):
        """
        Get a string representation of this model instance.
        """
        # TODO: return a string appropriate for the data fields
        return '<Greeting, ID: {}>'.format(self.id)

