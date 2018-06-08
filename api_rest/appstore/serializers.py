from rest_framework import serializers

from .models import Libro, Autor, Idioma, Pais, Editorial


class LibroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Libro
        fields = ('id', 'titulo', 'resumen', 'num_paginas', 'editorial',
                  'idiomas', 'autores', 'created_at', 'updated_at')
        depth = 3


class AutorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Autor
        fields = ('id', 'nombre', 'birth_year', 'genero', 'hair_color',
                  'idiomas', 'nacionalidad', 'created_at', 'updated_at')
        depth = 2


class PaisSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pais
        fields = ('id', 'nombre', 'acronimo','gentilicio', 'num_habitantes', 'created_at', 'updated_at')
        depth = 1


class IdiomaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Idioma
        fields = ('id', 'nombre', 'descripcion','pais', 'created_at', 'updated_at')
        depth = 1


class EditorialSerializer(serializers.ModelSerializer):

    class Meta:
        model = Editorial
        fields = ('id', 'nombre', 'descripcion', 'estado', 'created_at', 'updated_at')
        #fields = '__all__'
