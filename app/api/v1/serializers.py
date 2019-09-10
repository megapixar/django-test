from django.utils import timezone
from django.utils.datetime_safe import datetime
from rest_framework import serializers
from api import models


class MemberHappinessSerializer(serializers.ModelSerializer):

    def validate(self, data):
        """
        Check that start is before finish.
        """
        team_member = self.context['request'].user.team_member
        if team_member.last_happiness:
            can_add = datetime.now(timezone.utc).date() != team_member. \
                last_happiness.created_at.date()
        else:
            can_add = True

        if not can_add:
            raise serializers.ValidationError(
                "You can update happiness only once per day")
        return data

    def create(self, validated_data):
        member = self.context['request'].user.team_member
        return member.happiness.create(**validated_data)

    class Meta:
        model = models.MemberHappiness
        fields = ['happiness']
