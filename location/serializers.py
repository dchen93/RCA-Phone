from location.models import Phone, Center
from rest_framework import serializers
from django.utils import timezone


class CenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Center
        fields = ('center_name', 'current_location')


class PhoneSerializer(serializers.ModelSerializer):
    center_set = CenterSerializer(many = True)

    class Meta:
        model = Phone
        fields = ('phone_name', 'updated_time', 'center_set')

    def update(self, instance, validated_data):
        instance.phone_name = validated_data.get('phone_name', instance.phone_name)
        instance.updated_time = timezone.now()
        centers = validated_data.get('center_set', instance.center_set)

        for center in Center.objects.all():
        	for passedCenter in centers:
        		if (center.center_name == passedCenter.get('center_name')):
        			center.current_location = passedCenter.get('current_location')
        			center.save()
        			break

        instance.save()
        return instance