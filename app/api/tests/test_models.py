from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
from django.test import TestCase
from api.models import Team, TeamMember


class TeamModelTest(TestCase):

    def setUp(self):
        self.team = Team(name="Name")
        self.team.save()

    def test_string_representation(self):
        self.assertEqual(str(self.team), self.team.name)

    def test_created_slug(self):
        self.assertEqual(slugify(self.team.name), self.team.slug)

    def test_no_edited_slug(self):
        slug = self.team.slug
        self.team.name = "Name edited"
        self.team.save()
        self.assertEqual(slug, self.team.slug)

    def test_last_happiness_none(self):
        slug = self.team.slug
        self.team.name = "Name edited"
        self.team.save()
        self.assertEqual(slug, self.team.slug)


class TeamMemberModelTest(TestCase):

    def setUp(self):
        self.team = Team(name="Name")
        self.team.save()
        user = get_user_model()()
        user.username = 'username'
        user.save()
        self.team_member = TeamMember(team=self.team, user=user)
        self.team_member.save()

    def test_last_happiness_none(self):
        self.assertIsNone(self.team_member.last_happiness)

    def test_last_happiness_exists(self):
        self.team_member.happiness.create(happiness=1)
        self.assertIsNotNone(self.team_member.last_happiness)

    def test_team_slug(self):
        self.assertEqual(self.team_member.team_slug, self.team.slug)
