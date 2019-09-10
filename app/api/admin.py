from django.contrib import admin

from api import models


@admin.register(models.Team)
class HeroAdmin(admin.ModelAdmin):
    readonly_fields = ["slug"]


admin.site.register(models.TeamMember)
