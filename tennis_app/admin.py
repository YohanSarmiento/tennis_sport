from django.contrib import admin
from .models import *

# Register your models here.

class TournamentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "date", "location", "description")

class VenueAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "address", "phone", "schedule")

class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "instructor", "schedule", "description")

admin.site.register(Tournament, TournamentAdmin)
admin.site.register(Venue, VenueAdmin)
admin.site.register(Course, CourseAdmin)