from django.contrib.auth.models import User, Group
from images.models import images
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = images
        fields = ('url', 'author', 'title', 'text')