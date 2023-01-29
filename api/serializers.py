from rest_framework import serializers

from rest_framework.validators import UniqueValidator

from django.contrib.auth.password_validation import validate_password


from .models import User, Profile, LoanBook

""" 
Serializers allow complex data to be converted into native Python data types that can be rendered into JSON
ModelSerializers handle data validation automatically
 """


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "is_staff",
            "phone_number",
        ]


# User registration serializer


class RegisterUserSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User

        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "password",
            "confirm_password",
        ]
        extra_kwargs = {
            "first_name": {"required": True},
            "last_name": {"required": True},
        }

    def validate(self, attrs):

        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError("Password do not match")
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            phone_number=validated_data["phone_number"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class LoanBookSerializer(serializers.ModelSerializer):
    # remember the logged in user as the owner
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = LoanBook
        fields = "__all__"
