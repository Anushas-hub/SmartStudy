from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token


@api_view(['POST'])
def login_user(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)

    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "token": token.key,
            "username": user.username
        })
    else:
        return Response(
            {"error": "Invalid credentials"},
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['GET'])
def current_user(request):
    if request.user.is_authenticated:
        return Response({
            "username": request.user.username,
            "profile": {
                "credits": request.user.profile.credits,
                "level": request.user.profile.level,
                "badge": request.user.profile.badge,
            }
        })
    else:
        return Response(
            {"error": "Not authenticated"},
            status=status.HTTP_401_UNAUTHORIZED
        )
