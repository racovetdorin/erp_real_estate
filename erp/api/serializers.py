import re
from users.models import User
from rest_framework import serializers
from django.contrib.auth import password_validation


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'groups']


def validate_name(value):
    pattern = r'^[a-zA-Z0-9_\-\. ]*$'
    if not re.match(pattern, value):
        raise serializers.ValidationError('Names should not contain any special character.')
    return value


class UserCreateSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=150, required=True, validators=[validate_name])
    last_name = serializers.CharField(max_length=150, required=True, validators=[validate_name])
    email = serializers.EmailField(required=True)
    password = serializers.CharField(max_length=128, required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('User with this email already exist.')
        return value

    def validate_password(self, value):
        password_validation.validate_password(value, self.instance)
        return value

    def create(self, validated_data):
        email = validated_data['email']
        password = validated_data['password']
        del validated_data['email']
        del validated_data['password']
        created_user = User.objects.create_user(email=email, password=password, **validated_data)
        return created_user


class UserUpdateSerializer(UserCreateSerializer):
    id = serializers.IntegerField(required=True)
    first_name = serializers.CharField(max_length=150, required=False, validators=[validate_name])
    last_name = serializers.CharField(max_length=150, required=False, validators=[validate_name])
    email = serializers.EmailField(required=False)
    password = None

    class Meta:
        fields = ['id', 'first_name', 'last_name', 'email']

    def update(self, instance, validated_data):
        instance.update(**validated_data)
