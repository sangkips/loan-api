from django.urls import path, include
from rest_framework import routers

from .views import UserViewSet, UserProfileViewSet

router = routers.DefaultRouter()
router.register("user", UserViewSet)
router.register("profile", UserProfileViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
