from django.template.defaultfilters import slugify
from django.test import TestCase

from ..models import Team


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
