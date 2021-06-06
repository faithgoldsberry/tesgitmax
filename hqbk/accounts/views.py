from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from accounts.serializers import UserSerializer

class UserViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
