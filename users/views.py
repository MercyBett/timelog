from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from core.permissions import IsOwnerOrAdminOrReadOnly
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework import viewsets


class RegisterView(APIView):
    # permission_classes = (permissions.AllowAny,)

    def post(self, request):
        try:
            data = request.data

            email = data['email']
            email = email.lower()
            password = data['password']
            password2 = data['password2']

            if password != password2:
                return Response(
                    {'error': 'Passwords do not match'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            if len(password) >= 8:
                if not User.objects.filter(email=email).exists():
                    name = data['name']
                    User.objects.create_user(
                            email=email, name=name, password=password)
                    return Response(
                            {'success': 'User created successfully'},
                            status=status.HTTP_201_CREATED)

                else:
                    return Response(
                        {'error': 'User with this email already exists'},
                        status=status.HTTP_400_BAD_REQUEST
                    )
            else:
                return Response(
                    {'error': 'Password has to be at least 8 characters long'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except Exception:
            return Response(
                {'error': 'Something went wrong when registering the user'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class RetrieveView(APIView):
    def get(self, request, format=None):
        try:
            user = request.user
            user = UserSerializer(user)

            return Response(
                {'user': user.data},
                status=status.HTTP_200_OK
            )
        except Exception:
            return Response(
                {'error': 'Something went wrong when retrieving the user'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class UserViewSet(viewsets.ReadOnlyModelViewSet):

    permission_classes = [IsAuthenticated, IsOwnerOrAdminOrReadOnly]

    queryset = User.objects.all()
    serializer_class = UserSerializer