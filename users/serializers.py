from dataclasses import fields
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.hashers import make_password
from users.models import User


class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)

        data["access"] = str(refresh.access_token)
        data["refresh"] = str(refresh)

    
        data["Phone"] = self.user.Phone
        data["Name"] = self.user.Name
        return data

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [ "Name", "Address", "Phone", "password"]

    def create(self, validated_data):
        user = User(
            Name=validated_data["Name"],
            Address=validated_data["Address"],
            Phone=validated_data["Phone"],
            password=make_password(validated_data["password"]),
        )
        user.save()
        return user