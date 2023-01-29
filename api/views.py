from rest_framework import viewsets, permissions


from .models import User, Profile, LoanBook
from .serializers import (
    UserSerializer,
    ProfileSerializer,
    LoanBookSerializer,
    RegisterUserSerializer,
)

from .permissions import IsOwner


# viewsets define views behaviour, viewSets provide .list() and .create() methods automatically
# modelViewset provides .list(), .create(), .retrieve(), .partial_update() and .destroy() methods out of the box
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserRegisterViewSet(viewsets.ModelViewSet):
    """
    API endpoint for user registration
    """

    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer
    permission_classes = [
        permissions.AllowAny,
    ]


class UserProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows user profile to be created viewd, edited or deleted depending
    on the permission the user has.
    """

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]


# API endpoint for Loan creation
class UserLoanBookViewSet(viewsets.ModelViewSet):

    queryset = LoanBook.objects.all()
    serializer_class = LoanBookSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    # Associate loans with a given user
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
