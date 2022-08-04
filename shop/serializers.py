from rest_framework import serializers
from .models import Product, Comment, Like

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ['user']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["user"] = instance.user.email
        return rep

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        exclude = '__all__'
