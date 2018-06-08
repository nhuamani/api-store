from django.db import models


class Pais(models.Model):
    nombre = models.CharField(max_length=50)
    acronimo = models.CharField(max_length=5)
    gentilicio = models.CharField(max_length=25)
    num_habitantes = models.IntegerField()

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Pais"
        verbose_name_plural = "Paises"

    def __str__(self):
        return self.nombre


class Idioma(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250, null=True, blank=True)
    pais = models.ManyToManyField(Pais)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Idioma"
        verbose_name_plural = "Idiomas"

    def __str__(self):
        return self.nombre


class Editorial(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50, null=True, blank=True)
    estado = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Editorial"
        verbose_name_plural = "Editoriales"

    def __str__(self):
        return self.nombre


class Autor(models.Model):

    FEMALE = 'F'
    MALE = 'M'
    GENDER_CHOICES = (
        (FEMALE, 'Female'),
        (MALE, 'Male'),
    )
    nombre = models.CharField(max_length=255)
    birth_year = models.DateField()
    genero = models.CharField(max_length=7, choices=GENDER_CHOICES, default=MALE,)
    hair_color = models.CharField(max_length=50)
    idiomas = models.ManyToManyField(Idioma)
    nacionalidad = models.ManyToManyField(Pais)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    titulo = models.CharField(max_length=255)
    resumen = models.TextField()
    isbn = models.CharField(max_length=50)
    anio_edicion = models.CharField(max_length=20)
    num_paginas = models.CharField(max_length=5)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    idiomas = models.ManyToManyField(Idioma)
    autores = models.ManyToManyField(Autor)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"

    def __str__(self):
        return self.titulo
