from rest_framework.viewsets import ModelViewSet

from profiles.models import Profile
from profiles.serializers import ProfileSerializer


class ProfileListView(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
