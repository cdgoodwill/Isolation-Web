from django.contrib import admin

from .models import Place, User, UserConnection


class UserConnectionAdmin(admin.TabularInline):
    model = UserConnection


class UserAdmin(admin.ModelAdmin):
    ordering = ['email']

    list_display = ('email', 'place')

    inlines = [UserConnectionAdmin]


class InlineUserAdmin(admin.TabularInline):
    model = User

    ordering = ['email']


class PlaceAdmin(admin.ModelAdmin):
    ordering = ['house_name']

    list_display = ('house_name', 'zip_code')

    inlines = [InlineUserAdmin]


admin.site.register(Place, PlaceAdmin)
admin.site.register(User, UserAdmin)
#admin.site.register(UserConnection, UserConnectionAdmin)
