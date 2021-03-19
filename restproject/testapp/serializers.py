from rest_framework import serializers
from testapp.models import Artical


class ArticalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artical
        fields = ['title', 'author', 'email',]
