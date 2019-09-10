from django.contrib import admin

from api import models


@admin.register(models.Team)
class HeroAdmin(admin.ModelAdmin):
    readonly_fields = ["slug"]
    list_display = ('name', 'slug')


@admin.register(models.TeamMember)
class HeroAdmin(admin.ModelAdmin):
    list_display = ('user', 'team')
