from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer

class ProfileList(APIView):
    """
    Profile List API View for retrieving profiles.
    """

    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True, context={"request": request})
        return Response(serializer.data)


class ProfileDetail(APIView):
    """
    Profile Detail API View for retrieving and updating profiles.
    """

    serializer_class = ProfileSerializer

    def get(self, request, id):
        profile = get_object_or_404(Profile, id=id)
        serializer = ProfileSerializer(profile, context={"request": request})
        return Response(serializer.data)
