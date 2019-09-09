from django.contrib import admin

from .models import Team, TeamMember


@admin.register(Team)
class HeroAdmin(admin.ModelAdmin):
    readonly_fields = ["slug"]


admin.site.register(TeamMember)
