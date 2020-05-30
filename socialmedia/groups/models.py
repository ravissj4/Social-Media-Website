from django.db import models
# slugify helps in making normal sentences as links by adding 
# underscores in place of spaces and making everything lowercase
# and removing unwanted chars.
from django.utils.text import slugify

from django.core.urlresolvers import reverse

# Groups models.py
# Create your models here.

# misaka is used for markdows inside of posts
import misaka

# get_user_model helps in grabbing the current user in the current user 
# session
from django.contrib.auth import get_user_model
User = get_user_model()

# this is to use custom template tags used in posts/templates/posts/post_list.html
# it allows to grab the details from this model to give to that app
# specifically here inside GroupMember model, user_group can be grabbed by 
# get_user_group inside that post_list.html tempalte
from django import template
register = template.Library()


class GroupMember(models.Model):
    group = models.ForeignKey(Group, related_name='memberships')
    user = models.ForeignKey(User, related_name='user_group')

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('group', 'user')
    

class Group(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=False, default='')
    description_html = models.TextField(editable=True, default='', blank=True)
    members = models.ManyToManyField(User, through='GroupMember')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("groups:single", kwargs={"slug": self.slug})

    class Meta:
        ordering = 'name'    
    