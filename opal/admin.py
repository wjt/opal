"""
Combined admin for OPAL models
"""
from django.contrib import admin
from django.contrib.contenttypes import generic
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

import reversion

from opal.models import option_models, Synonym
from opal.models import UserProfile

from opal import models

admin.site.unregister(User)

class UserProfileInline(admin.StackedInline):
    model = UserProfile

class UserProfileAdmin(UserAdmin):
    inlines = [ UserProfileInline, ]

class MyAdmin(reversion.VersionAdmin): pass

class PatientSubRecordAdmin(reversion.VersionAdmin):
    list_filter = ['patient']

class EpisodeSubRecordAdmin(reversion.VersionAdmin):
    list_filter = ['episode']

class SynonymInline(generic.GenericTabularInline):
    model = Synonym

class OptionAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']
    inlines = [SynonymInline]

for model in option_models.values():
    admin.site.register(model, OptionAdmin)

admin.site.register(User, UserProfileAdmin)
admin.site.register(models.Patient, MyAdmin)
admin.site.register(models.Episode, MyAdmin)i

for subclass in models.PatientSubrecord.__subclasses__():
    admin.site.register(subclass, PatientSubRecordAdmin)

for subclass in models.EpisodeSubrecord.__subclasses__():
    admin.site.register(subclass, EpisodeSubRecordAdmin)
