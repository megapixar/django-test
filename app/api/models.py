from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify


class Team(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class TeamMember(models.Model):
    user = models.OneToOneField(get_user_model(), related_name='team_member',
                                on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    @property
    def team_slug(self):
        return self.team.slug

    @property
    def last_happiness(self):
        if self.happiness.count() == 0:
            return None

        return self.happiness.latest('created_at')


class MemberHappiness(models.Model):
    UNHAPPY = 1
    NEUTRAL = 3
    HAPPY = 5
    HAPPINESS_LEVEL = [
        (UNHAPPY, 'Unhappy'),
        (NEUTRAL, 'Neutral'),
        (HAPPY, 'Very Happy'),
    ]
    member = models.ForeignKey(TeamMember, on_delete=models.CASCADE,
                               related_name='happiness')
    happiness = models.IntegerField(choices=HAPPINESS_LEVEL)
    created_at = models.DateTimeField(auto_now_add=True)
