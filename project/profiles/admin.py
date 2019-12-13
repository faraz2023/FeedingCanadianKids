from django.contrib import admin
from profiles.models import Profile
from profiles.models import BasicUser

# Register your models here.
admin.site.register(Profile)
admin.site.register(BasicUser)
