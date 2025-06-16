# users/views.py
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['POST'])
def register(request):
    username = request.data['username']
    password = request.data['password']
    email = request.data.get('email', '')

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Utilisateur existe déjà'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, password=password, email=email)
    return Response({'message': 'Inscription réussie'})
