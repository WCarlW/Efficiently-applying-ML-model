from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Dweet, Profile, Sentiment

class ProfileInline(admin.StackedInline):
    model = Profile

class DweetInline(admin.StackedInline):
    model = Dweet
    fields = []

class DweetAdmin(admin.ModelAdmin):
    readonly_fields = ['sentiment']

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]
    inlines = []

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
admin.site.register(Dweet, DweetAdmin)
admin.site.register(Sentiment)