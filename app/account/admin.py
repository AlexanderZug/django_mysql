from django.contrib import admin

from .models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'age', 'city', 'get_multiply_age')
    list_per_page = 10

    @admin.display(description='Multiply age')
    def get_multiply_age(self, obj) -> int:
        return obj.age * 2
