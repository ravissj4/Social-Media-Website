from django.db import models

# Posts models.py

# Create your models here.

from django.core.urlresolvers import reverse

import misaka

from groups.models import Group 

from django.contrib.auth import get_user_model
User = get_user_model()

class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts')
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    # not making message_html editable as I want it to take value directly from 
    # the message text
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(Group, related_name='posts')

    def __str__(self):
        return self.message
    
    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)

    def get_absolute_url(self):
        return reverse("posts:single", kwargs={"username" : self.user.username, "pk": self.pk})

    class Meta:
        # the - infront makes the ordering in descending order based on dates
        ordering = ['-created_at']
        # this way each message will be tied to a user
        unique_together = ['user', 'message']



    
    