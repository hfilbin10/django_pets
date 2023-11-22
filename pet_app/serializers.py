from rest_framework import serializers
from .models import Owner, Cat, Bird, Dog, Exotic_animal


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ["id", "name", "age" "number_of_pets"]


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = ["id", "name", "age" "breed", "vaccinated", "description"]


class BirdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bird
        fields = ["id", "name", "age" "vaccinated", "description", "species"]


class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = ["id", "name", "age" "vaccinated", "breed", "description"]


class Exotic_animalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exotic_animal
        fields = ["id", "name", "age" "vaccinated", "region_of_origin", "type_of_animal"]
