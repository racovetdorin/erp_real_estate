from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser')


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('first_name', 'last_name', 'email')
    ordering = ['email']
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'first_name',
                'last_name',
                'groups',
                'password1',
                'password2',
                'is_staff',
                'is_superuser',
            ),
        }),
    )
    fieldsets = (
        (None, {
            'fields': (
                ('email', 'first_name', 'last_name', 'groups', 'is_staff', 'is_superuser')
            ),
        }),
    )
