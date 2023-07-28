from rest_framework import serializers
from .models import metamodels


class metaSerializer(serializers.ModelSerializer):

    class Meta:
        model = metamodels
        fields = "__all__"



     