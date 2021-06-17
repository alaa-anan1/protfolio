from django.contrib import admin
from about_page.models import About, Trip

# Register your models here.

class AboutAdmin(admin.ModelAdmin):
    pass

class TripAdmin(admin.ModelAdmin):
    pass

admin.site.register(About, AboutAdmin)
admin.site.register(Trip, TripAdmin)