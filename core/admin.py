from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.



admin.site.register(User)
# admin.site.register(Product)
admin.site.unregister(Group)
# admin.site.register(Order)
# admin.site.register(OrderProduct)
# admin.site.register(Studant)
# admin.site.register(Teacher)
# admin.site.register(Course)