from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from .models import User, Profile


class UserReqisterSerializer(serializers.ModelSerializer):

    phone_number = serializers.CharField(max_length=13)
    short_info = serializers.CharField()
    password2 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ["username", "password", "profile_image", "phone_number", "short_info", "password2"]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        password = data.get('password', '')
        password2 = data.get('password2', '')
        errors = {}
        if password != password2:
            errors['password'] = "Пароли не совпадают"
        if not all([
            len(password) >= 8,
            any(char.isdigit() for char in password),
            any(char.isupper() for char in password),
            any(char.islower() for char in password),
            any(char in '!@#$%^&*()_+-=[]{}|;:,.<>?/~`' for char in password)
        ]):
            errors[
                'password'] = "Пароль должен быть не менее 8 символов и содержать хотя бы одну цифру, одну заглавную и одну прописную букву, один специальный символ"
        if errors:
            raise serializers.ValidationError(errors)
        return data

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],

        )
        profile_image = validated_data.get('profile_image')
        if profile_image:
            user.profile_image = profile_image
        user.set_password(validated_data['password'])
        user.save()
        try:
            profile = Profile.objects.create(
                user=user,
                phone_number=validated_data['phone_number'],
                short_info=validated_data['short_info'],
            )
        except Exception as e:
            user.delete()
            raise e
        else:
            profile.username = user.username
            profile.profile_image = user.profile_image
        return profile




