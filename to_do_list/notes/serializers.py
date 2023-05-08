"""
This file contains the serializers of Note and User entity
"""
from rest_framework import serializers
from django.contrib.auth.models import User
from notes.models import Note


class NoteSerializer(serializers.Serializer):
    """
    This is the serializer of Note
    """
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    description = serializers.CharField(required=False, allow_blank=True, max_length=1000)
    owner = serializers.ReadOnlyField(source='owner.username')
   
    class Meta:
        model = Note
        fields = ['id', 'title', 'description', 'owner']
	

    def create(self, validated_data):
        """
        Create and return a new `Note` instance, given the validated data.
        """
        return Note.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """
        Update and return an existing `Note` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    """
    This is the serializer of User
    """
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        """
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')