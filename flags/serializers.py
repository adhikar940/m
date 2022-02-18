from . models import *
from rest_framework import serializers
class flagSerializers(serializers.ModelSerializer):
    class Meta:
        model = flag
        fields = ['id','Status','Highlight', 'color', 'url', 'videourl', 'name']
class flag1Serializers(serializers.ModelSerializer):
    class Meta:
        model = flag1
        fields = ['name','activate', ]
