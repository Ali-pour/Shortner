from django.contrib import admin
from .models import Short_link, Full_link


admin.site.register(Full_link)
admin.site.register(Short_link)
