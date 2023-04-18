from rest_framework import serializers
from .models import Project

class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id','español','ashaninka','pronunciacion')
        read_onli_fields = ('created_at',)