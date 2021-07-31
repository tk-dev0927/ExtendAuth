from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from .models import User, StaffGroup

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(StaffGroup, GroupAdmin)