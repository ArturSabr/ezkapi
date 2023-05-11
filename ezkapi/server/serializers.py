from rest_framework import serializers
from .models import *
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'username', 'first_name', 'last_name', 'middle_name', 'email', 'password']

    def create(self, validated_data):
        try:
            gender = validated_data['gender']
        except:
            gender = None

        user = Student.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            middle_name=validated_data['middle_name'],
            gender=gender
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class UpdateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    username = serializers.CharField(required=False)
    gender = serializers.CharField(required=False)
    date_of_birth = serializers.DateField(required=False)

    class Meta:
        model = Student
        fields = ('username', 'first_name', 'last_name', 'middle_name', 'email')

    def update(self, instance, validated_data):
        user = self.context['request'].user

        if user.pk != instance.pk:
            raise serializers.ValidationError({"authorize": "You dont have permission for this user."})
        print(user)
        return super().update(instance, validated_data)


class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Student
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):

        instance.set_password(validated_data['password'])
        instance.save()

        return instance
