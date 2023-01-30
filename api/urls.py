from django.urls import path, include


from rest_framework import routers


from .views import (
    UserProfileViewSet,
    UserRegisterViewSet,
    UserLoanBookViewSet,
    UserViewSet,
    UserLoginViewset,
)


# routers provide an easy way to automatically determine url conf
# DefaultRouter returns a response containing hyperlinks to all list views

router = routers.DefaultRouter()
router.register("users", UserViewSet, basename="user")
router.register("profile", UserProfileViewSet, basename="profile")
router.register("loan", UserLoanBookViewSet, basename="loan")
router.register("register", UserRegisterViewSet, basename="register")
router.register("login", UserLoginViewset, basename="login")

urlpatterns = [
    path("", include(router.urls)),
]
