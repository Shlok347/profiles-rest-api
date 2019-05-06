from rest_framework import serializers
from . import models

class HelloSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=32)
    imei = serializers.CharField(max_length=32)

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = ('id','email', 'name', 'password', 'user_password', 'imei', 'lock_password', 'master_id', 'master_password')
        extra_kwargs = {'password': {'write_only':True}}

    def create(self, validated_data):
        user = models.UserProfile (
            email = validated_data['email'],
            name = validated_data['name'],
            # password = validated_data['password'],
            user_password = validated_data['user_password'],
            imei = validated_data['imei'],
            lock_password = validated_data['lock_password'],
            master_id = validated_data['master_id'],
            master_password = validated_data['master_password'],

        )
        user.set_password(validated_data['password'])
        user.save()

        return user

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}
