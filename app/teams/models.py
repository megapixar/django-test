from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth import get_user_model


class Team(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class TeamMember(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    happiness = models.IntegerField(blank=True, null=True,
                                    validators=[MinValueValidator(1),
                                                MaxValueValidator(5)])
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True,
                             blank=True)

    def __str__(self):
        return self.user.username


class MemberHappiness(models.Model):
    member = models.ForeignKey(TeamMember, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
