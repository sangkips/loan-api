from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.request import Request

from .models import User, Profile, LoanBook
from .serializers import (
    UserSerializer,
    ProfileSerializer,
    LoanBookSerializer,
    RegisterUserSerializer,
    LoginSerializer,
)
from .token import auth_token
from .permissions import IsOwner


# viewsets define views behaviour, viewSets provide .list() and .create() methods automatically
# modelViewset provides .list(), .create(), .retrieve(), .partial_update() and .destroy() methods out of the box
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# User registration view
class UserRegisterViewSet(viewsets.ModelViewSet):
    """
    API endpoint for user registration
    """

    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer
    permission_classes = [
        permissions.AllowAny,
    ]


# Login view
class UserLoginViewset(viewsets.ModelViewSet):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token = auth_token(user)
        return Response({"token": token})


# User Profile view
class UserProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows user profile to be created viewd, edited or deleted depending
    on the permission the user has.
    """

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]


# Loan View
class UserLoanBookViewSet(viewsets.ModelViewSet):

    queryset = LoanBook.objects.all()
    serializer_class = LoanBookSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    # Associate loans with a given user
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
