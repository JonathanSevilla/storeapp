from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from django_otp.plugins.otp_totp.models import TOTPDevice
from rest_framework.response import Response
import pyotp

@api_view(['POST'])
def generate_otp(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    # authenticate user
    user = authenticate(username=username, password=password)
    if user is None:
        return Response({'error': 'Invalid credentials'})
    
    # generate one-time password
    secret_key = pyotp.random_base32()
    totp = pyotp.TOTP(secret_key)
    otp = totp.now()
    
    return Response({'Token': otp})