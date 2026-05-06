from django.contrib import admin
from bciitapp.models import *

admin.site.register(Enquiry)

class ClubImageInline(admin.TabularInline):
    model = ClubImage
    extra = 3

class ClubAdmin(admin.ModelAdmin):
    inlines = [ClubImageInline]

admin.site.register(Club, ClubAdmin)


# FACULTY
class FacultyImageInline(admin.TabularInline):
    model = FacultyImage
    extra = 3

class FacultyAdmin(admin.ModelAdmin):
    inlines = [FacultyImageInline]

admin.site.register(Faculty, FacultyAdmin)


# EVENT
class EventImageInline(admin.TabularInline):
    model = EventImage
    extra = 3

class EventAdmin(admin.ModelAdmin):
    inlines = [EventImageInline]

admin.site.register(Event, EventAdmin)
