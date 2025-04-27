from django.contrib import admin
from .models import Story

class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'summary')  # These fields must exist in the model
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Story, StoryAdmin)
