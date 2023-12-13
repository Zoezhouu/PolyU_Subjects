from rest_framework import viewsets, status
from django.contrib.auth.models import User
from .UserSerializer import UserSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        
        # Create a token for the newly created user
        user = User.objects.get(username=serializer.validated_data['username'])
        token, created = Token.objects.get_or_create(user=user)

        # Exclude the password field from the response
        data = serializer.data
        data.pop('password')

        # Include user ID, is_admin, and token in the response
        data['user_id'] = user.id
        data['is_staff'] = user.is_staff  # Assumes is_admin is based on staff status
        data['token'] = token.key

        return Response(data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        # Hash the password before saving the user
        user = serializer.save()
        user.set_password(serializer.validated_data['password'])
        user.save()
