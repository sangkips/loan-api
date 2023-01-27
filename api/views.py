from rest_framework import viewsets

from .models import CustomUser, Profile, LoanBook
from .serializers import UserSerializer, ProfileSerializer, LoanBookSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class UserLoanBookViewSet(viewsets.ModelViewSet):
    queryset = LoanBook.objects.all()
    serializer_class = LoanBookSerializer
