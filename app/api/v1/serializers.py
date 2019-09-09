from django.utils import timezone
from django.utils.datetime_safe import datetime
from rest_framework import serializers
from ..models import MemberHappiness


class MemberHappinessSerializer(serializers.ModelSerializer):

    def validate(self, data):
        """
        Check that start is before finish.
        """
        user = self.context['request'].user
        can_add = False
        if user.team_member.happiness.count() > 0:
            latest_happiness = user.team_member.happiness.latest('created_at')
            can_add = datetime.now(timezone.utc).date() != \
                      latest_happiness.created_at.date()

        if not can_add:
            raise serializers.ValidationError(
                "You can update happiness once a day")
        return data

    def create(self, validated_data):
        member = self.context['request'].user.team_member
        return member.happiness.create(**validated_data)

    class Meta:
        model = MemberHappiness
        fields = ['happiness']
