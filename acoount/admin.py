from django.contrib import admin
from acoount.models import CustomUser, Contact


admin.site.register(CustomUser)
admin.site.register(Contact)