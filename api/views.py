from rest_framework.response import Response
from rest_framework.views import APIView
from . import serializers
from .models import Cheff, Recipe 
from django.http import Http404
from rest_framework import status


class Cheffs(APIView):

    def get(self, request):
        cheff = Cheff.objects.all()
        serializer = serializers.CheffSerializer(cheff, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.CheffSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CheffsDetail(APIView):

    def get(self, request, cheff_id):
        try:
            cheff = Cheff.objects.get(pk=cheff_id)
        except Cheff.DoesNotExist:
            raise Http404
        serializer = serializers.CheffSerializer(cheff)
        return Response(serializer.data)

    def delete(self, request, cheff_id):
        try:
            cheff = Cheff.objects.get(pk=cheff_id)
        except Cheff.DoesNotExist:
            raise Http404
        cheff.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Recipes(APIView):

    def get(self, request, cheff_id):
        recipes = Recipe.objects.filter(cheff_id=cheff_id)
        serializer = serializers.RecipeSerializer(recipes, many=True)
        return Response(serializer.data)

    def post(self, request, cheff_id):
        try:
            Cheff.objects.get(pk=cheff_id)
        except Cheff.DoesNotExist:
            raise Http404

        serializer = serializers.RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(cheff_id=cheff_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RecipeDetail(APIView):

    def get(self, request, cheff_id, recipe_id):
        try:
            recipe = Recipe.objects.get(cheff_id=cheff_id, pk=recipe_id)
        except Recipe.DoesNotExist:
            raise Http404
        serializer = serializers.RecipeSerializer(recipe)
        return Response(serializer.data)

    def delete(self, request, cheff_id, recipe_id):
        try:
            recipe = Recipe.objects.get(cheff_id=cheff_id, pk=recipe_id)
        except Recipe.DoesNotExist:
            raise Http404
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
