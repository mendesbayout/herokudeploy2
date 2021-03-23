from rest_framework import serializers
from . import models
import base64
from django.conf import settings
import os


class CheffSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cheff
        fields = ['id', 'direction', 'phone']


class RecipeSerializer(serializers.ModelSerializer):
    #thumbnail = serializers.SerializerMethodField('encode_thumbnail') - IMPLEMENTAR THUMBNAILS NO FUTURO QUANDO TIVER TEMPO
    #def encode_thumbnail(self, recipe):
        #with open(os.path.join(settings.MEDIA_ROOT, recipe.thumbnail.name), "rb") as image_file:
            #return base64.b64encode(image_file.read())


    def create(self, validated_data):
        cheff = models.cheff.objects.get(pk=validated_data["cheff_id"])
        validated_data["cheff"] = cheff
        #recipe = models.Recipe.objects.create(**validated_data)
        receita = models.Recipe.object.get(pl=validated_data["receita"])
        return recipe

    class Meta:
        model = models.Recipe
        fields = ['id', 'receita', 'cheff', ]
