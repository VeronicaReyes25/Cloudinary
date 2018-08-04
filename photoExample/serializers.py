from photoExample.models import photoExample
from rest_framework import serializers

class PhotoExampleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = photoExample
        fields = ('id','url', 'created_date')