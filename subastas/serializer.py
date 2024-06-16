from django.forms import ValidationError
from rest_framework import serializers
from.models import Users, Addresses, UserTypes, Pictures, PaymentMethods

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addresses
        fields = [
            'address_id',
            'latitude',
            'longitude'
        ]

class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTypes
        fields = [
            'user_type_id',
            'user_type'
        ]

class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pictures
        fields = [
            'picture_id',
            'picture_address'
        ]

class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethods
        fields = [
            'payment_method_id',
            'payment_method_name'
        ]

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = [
            'user_id',
            'first_name',
            'second_name',
            'first_surname',
            'second_surname',
            'user_dni',
            'user_address',
            'verification',
            'user_type',
            'picture',
            'payment_method',
            'email',
            'password'
        ]