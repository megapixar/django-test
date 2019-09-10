from datetime import timedelta
from unittest.mock import Mock, MagicMock
from django.test import TestCase
from django.utils.datetime_safe import datetime
from rest_framework import serializers

from app.api.v1.serializers import MemberHappinessSerializer


class MemberHappinessSerializerTest(TestCase):

    def test_validate_no_happiness_exists(self):
        user = Mock()
        user.team_member.last_happiness = None

        context = MagicMock()
        context['request'].user = user

        serializer = MemberHappinessSerializer(data={'happiness': 5},
                                               context=context)
        data = {'happiness': 5}
        self.assertDictEqual(data, serializer.validate(data))

    def test_validate_happiness_was_set_today(self):
        happiness = Mock()
        happiness.created_at = datetime.today()

        user = Mock()
        user.team_member.last_happiness = happiness

        context = MagicMock()
        context['request'].user = user
        with self.assertRaises(serializers.ValidationError):
            serializer = MemberHappinessSerializer(context=context)
            serializer.validate({'happiness': 5})

    def test_validate_happiness_was_set_yesterday(self):
        happiness = Mock()
        happiness.created_at = datetime.today() - timedelta(days=1)

        user = Mock()
        user.team_member.last_happiness = happiness

        context = MagicMock()
        context['request'].user = user
        data = {'happiness': 5}
        serializer = MemberHappinessSerializer(context=context)
        self.assertDictEqual(data, serializer.validate(data))

    def test_create_happiness_to_logged_user(self):
        user = Mock()

        context = MagicMock()
        context['request'].user = user
        data = {'happiness': 5}
        MemberHappinessSerializer(context=context).create(data)

        user.team_member.happiness.create.assert_called_once_with(**data)
