from django.contrib import admin

# Register your models here.
from taskapp.models import WhyUs, Team

admin.site.register(WhyUs)
admin.site.register(Team)