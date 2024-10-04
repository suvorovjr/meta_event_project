from rest_framework import serializers
from .models import InstagramPages, FacebookPages


class FacebookPagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacebookPages
        fields = '__all__'


class InstagramPagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstagramPages
        fields = '__all__'
