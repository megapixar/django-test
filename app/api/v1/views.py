from rest_framework import generics
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from api import models
from api.v1.serializers import MemberHappinessSerializer

from api.queries import get_happiness_stat


class MemberHappiness(generics.ListCreateAPIView):
    serializer_class = MemberHappinessSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        slug = self.kwargs['team_slug']
        return models.MemberHappiness.objects.filter(member__team__slug=slug). \
            all()

    def get_response(self, slug):
        return Response({'data': get_happiness_stat(slug)}, 200)

    def get(self, request, *args, **kwargs):
        return self.get_response(kwargs.get('team_slug'))

    def post(self, request, *args, **kwargs):
        slug = kwargs.get('team_slug')
        if slug != request.user.team_member.team_slug:
            raise PermissionDenied()

        self.create(request, *args, **kwargs)

        return self.get_response(slug)
