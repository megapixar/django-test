from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import MemberHappinessSerializer
from .. import models


class MemberHappiness(generics.ListCreateAPIView):
    queryset = models.MemberHappiness.objects.all()
    serializer_class = MemberHappinessSerializer
    permission_classes = [IsAuthenticated]
