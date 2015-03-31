from location.models import Phone, Center
from rest_framework import serializers


class CenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Center
        fields = ('center_name', 'current_location')


class PhoneSerializer(serializers.ModelSerializer):
    center_set = CenterSerializer(many = True)

    class Meta:
        model = Phone
        fields = ('phone_name', 'updated_time', 'center_set')
