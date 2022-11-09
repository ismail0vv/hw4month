from django.contrib import admin
from .models import Film, Director


# Register your models here.
class FilmsInLine(admin.StackedInline):
    model = Film
    extra = 1


class FilmAdmin(admin.ModelAdmin):
    list_display = ['director', 'title', 'producer', 'rating', 'duration']
    search_fields = 'director title producer'.split()
    list_filter = 'director producer'.split()
    list_editable = 'rating duration'.split()
    list_per_page = 100


class DirectorAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']
    list_per_page = 100
    inlines = [FilmsInLine]


admin.site.register(Film, FilmAdmin)
admin.site.register(Director, DirectorAdmin)
