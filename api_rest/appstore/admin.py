from django.contrib import admin
from .models import Libro, Autor, Idioma, Pais, Editorial


class LibroAdmin(admin.ModelAdmin):
    list_display = ("titulo", "editorial", "created_at", "updated_at")

admin.site.register(Libro, LibroAdmin)
admin.site.register(Autor)
admin.site.register(Idioma)
admin.site.register(Pais)
admin.site.register(Editorial)
