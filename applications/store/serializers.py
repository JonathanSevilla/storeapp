from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from .models import (
    Brand,
    Stores,
    Deals,
    Subscription
)

class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = '__all__'


class StoresSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stores
        fields = '__all__'


class DealsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Deals
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    email = serializers.CharField(source='user.email', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Subscription
        fields = ('email','username','user','store')