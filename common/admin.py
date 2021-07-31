from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from .models import User, StaffGroup

# Register your models here.

# Adding UserAdmin, GroupAdmin 
# enable to select group on user change and to select permission on group change
admin.site.register(User, UserAdmin)
admin.site.register(StaffGroup, GroupAdmin)