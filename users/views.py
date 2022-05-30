from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import LoginSerializer, UserSerializer
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError

class Login(TokenObtainPairView):
    serializer_class = LoginSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            return Response(serializer.validated_data, status=status.HTTP_200_OK)

        except TokenError as e:
            raise InvalidToken(e.args[0])
        except Exception as e:
            print(e)


class Register(generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        try:
            user_serializer = self.serializer_class(data=request.data)
            if user_serializer.is_valid(raise_exception=True):
                user_serializer.save()
                return Response({"data": user_serializer.data}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)




