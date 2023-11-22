from django.db import models
from django.core import validators as v
from .validator import validate_name


class Owner(models.Model):
    name = models.CharField(
        max_length=255, null=False, blank=False, validators=[validate_name]
    )
    age = models.PositiveIntegerField(
        null=False,
        blank=False,
        validators=[v.MinValueValidator(1), v.MaxValueValidator(110)],
    )
    number_of_pets = models.PositiveIntegerField(null=False, blank=False)


class Cat(models.Model):
    breed = models.CharField(max_length=255, null=False, blank=False, default="Unknown")
    age = models.PositiveIntegerField(
        null=False,
        blank=False,
        validators=[v.MinValueValidator(0), v.MaxValueValidator(25)],
    )
    vaccinated = models.BooleanField(default=True)
    description = models.TextField()
    name = models.CharField(
        max_length=255, null=False, blank=False, validators=[validate_name]
    )


class Bird(models.Model):
    name = models.CharField(
        max_length=255, null=False, blank=False, validators=[validate_name]
    )
    age = models.PositiveIntegerField(
        null=False,
        blank=False,
        validators=[v.MinValueValidator(0), v.MaxValueValidator(50)],
    )
    vaccinated = models.BooleanField(default=True)
    description = models.TextField(null=False, blank=False)
    species = models.CharField(
        max_length=255, null=False, blank=False, default="Unknown"
    )


class Dog(models.Model):
    age = models.PositiveIntegerField(
        null=False,
        blank=False,
        validators=[v.MinValueValidator(1), v.MaxValueValidator(25)],
    )
    name = models.CharField(
        max_length=255, null=False, blank=False, validators=[validate_name]
    )
    vaccinated = models.BooleanField(default=True)
    breed = models.CharField(max_length=255, null=False, blank=False, default="Unknown")
    description = models.TextField(null=False, blank=False)


class Exotic_animal(models.Model):
    region_of_origin = models.CharField(
        max_length=255, null=False, blank=False, default="Unknown"
    )
    name = models.CharField(
        max_length=255, null=False, blank=False, validators=[validate_name]
    )
    age = models.PositiveIntegerField(
        null=False,
        blank=False,
        validators=[v.MinValueValidator(0), v.MaxValueValidator(25)],
    )
    type_of_animal = models.CharField(max_length=255, null=False, blank=False)
    vaccinated = models.BooleanField(default=True)
