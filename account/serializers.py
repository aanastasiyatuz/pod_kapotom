from tkinter.messagebox import RETRYCANCEL
from rest_framework import serializers 

from django.contrib.auth import get_user_model
 

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    
    password_confirm = serializers.Charfield()


    class Meta:
        model = User
        field = [
            'email', 'username', 'password', 
            'password_confirm'
        ]

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('User with this email already exists')
        return email

    def validate(self, attrs):
        p1 = attrs['password']
        p2 = attrs.pop('password_comfirm')

        if p1 != p2:
            raise serializers.ValidationError(
                'Password does not match'
            )

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
        