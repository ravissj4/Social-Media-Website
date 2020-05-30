from django.contrib import admin
from . import models


# groups admin.py 
# Register your models here.

# concept of a tabular inline :
# allows to edit the models on the same page as the parent model on the admin page
# like here GroupMember has parent model Group, so we can go to the admin page and see
# Groups and then edit GroupMembers as well using this way
class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember



admin.site.register(models.Group)
