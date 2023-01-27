from rest_framework import serializers
from .models import CustomUser, Profile, LoanBook


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser

        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "is_staff",
            "phone_number",
        ]


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class LoanBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanBook
        fields = "__all__"
