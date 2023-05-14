from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import *


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("email", "is_staff", "is_active",)
    list_filter = ("email", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("email", "password", 'first_name', 'last_name', 'middle_name', 'username')}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Student)
admin.site.register(Discipline)
admin.site.register(DSU)
admin.site.register(Urok)
admin.site.register(Direction)

admin.site.register(Faculty)
admin.site.register(Education)
admin.site.register(EduCategory)
admin.site.register(Positions)
admin.site.register(OtdelKadrovPPS)
admin.site.register(OtdelKadrovUchashiesya)
admin.site.register(MezhdunarodnyiOtdel)
admin.site.register(PriemnayaKomissiya)
admin.site.register(UchebnyiOtdel)
admin.site.register(VtoroiOtdel)
admin.site.register(Buhgalteriya)
admin.site.register(Dekanat)
admin.site.register(Prepodavatel)
admin.site.register(Roditeli)
admin.site.register(Kafedra)
admin.site.register(UMK)

