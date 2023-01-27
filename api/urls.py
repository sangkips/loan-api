from django.urls import path, include
from rest_framework import routers

from .views import UserViewSet, UserProfileViewSet, UserLoanBookViewSet

router = routers.DefaultRouter()
router.register("user", UserViewSet)
router.register("profile", UserProfileViewSet)
router.register("loan", UserLoanBookViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
