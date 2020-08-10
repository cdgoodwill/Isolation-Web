from django.contrib import admin

from .models import Place, Person, ConnectedPlace


class ConnectedPlaceAdmin(admin.TabularInline):
    model = ConnectedPlace


class PersonAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_display = ('name', 'covid_status', 'place')


class InlinePersonAdmin(admin.TabularInline):
    model = Person
    ordering = ['name']


class PlaceAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_display = ('name', 'zip_code')
    inlines = [InlinePersonAdmin, ConnectedPlaceAdmin]


admin.site.register(Place, PlaceAdmin)
admin.site.register(Person, PersonAdmin)
