import graphene
import logging

from graphene_django.types import DjangoObjectType

from .models import Libro, Autor, Editorial, Pais, Idioma


class LibroType(DjangoObjectType):

    class Meta:
        model = Libro


class AutorType(DjangoObjectType):

    class Meta:
        model = Autor


class EditorialType(DjangoObjectType):

    class Meta:
        model = Editorial


class PaisType(DjangoObjectType):

    class Meta:
        model = Pais

class IdiomaType(DjangoObjectType):
    
    class Meta:
        model = Idioma

class Query(graphene.AbstractType):

    all_libros = graphene.List(LibroType)
    all_autores = graphene.List(AutorType)
    all_editoriales = graphene.List(EditorialType)
    all_paises = graphene.List(PaisType)
    all_idiomas = graphene.List(IdiomaType)
    libro = graphene.Field(LibroType, id=graphene.Int(),isbn=graphene.String())
    autor = graphene.Field(AutorType, id=graphene.Int())

    def resolve_all_libros(self, info, *args):
        return Libro.objects.all()

    def resolve_all_autores(self, info, *args):
        return Autor.objects.all()

    def resolve_all_editoriales(self, info, *args):
        return Editorial.objects.all()

    def resolve_all_paises(self, info, *args):
        return Pais.objects.all()

    def resolve_all_idiomas(self, info, *args):
        return Idioma.objects.all()

    def resolve_libro(self, info, **kwargs):
        id = kwargs.get('id')
        isbn = kwargs.get('isbn')

        if id is not None:
            return Libro.objects.get(pk=id)

        if isbn is not None:
            return Libro.objects.get(isbn=isbn)

        return None

    def resolve_autor(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Autor.objects.get(pk=id)

        return None
