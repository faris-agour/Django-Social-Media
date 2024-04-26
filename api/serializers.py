from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from posts.models import Post
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',
                  'email', 'first_name', 'last_name')

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match")

        return data

    def create(self, validated_data):
        # Rem ove password1 and password2 from validated_data
        password1 = validated_data.pop('password1')
        password2 = validated_data.pop('password2')

        # Create a new user without password first
        user = User.objects.create_user(**validated_data)

        # Set password
        user.set_password(password1)
        user.save()

        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
