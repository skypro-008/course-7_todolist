from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from core.models import User


class CreateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_repeat = serializers.CharField(write_only=True)

    def validate(self, attrs: dict):
        res = super().validate(attrs)
        password: str = attrs.get("password")
        password_repeat: str = attrs.get("password_repeat")
        if password != password_repeat:
            raise ValidationError("password and password_repeat is not equal")
        return res

    class Meta:
        model = User
        read_only = ("id",)
        fields = ("id", "username", "first_name", "last_name", "email", "password", "password_repeat")
