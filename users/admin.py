from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['email', 'username', 'first_name', 'last_name', 'phone_number', 'department', 'designation']
    model = CustomUser


admin.site.register(CustomUser, CustomUserAdmin)
