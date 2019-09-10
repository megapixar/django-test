from unittest.mock import Mock

from rest_framework.exceptions import PermissionDenied
from rest_framework.test import APISimpleTestCase

from api.v1.views import MemberHappiness


class MemberHappinessTests(APISimpleTestCase):

    def test_submit_happiness_not_right_team(self):
        request = Mock()
        request.user.team_member.team_slug = 'team_slug'
        api = MemberHappiness()

        with self.assertRaises(PermissionDenied):
            api.post(request, team_slug='team_slug_wrong')
