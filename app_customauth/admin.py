from django.contrib import admin

from app_customauth.models import CustomUser


# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):

    list_display = ("created_date", "is_admin", "is_active", "login")

    fields = ("tb_person", "is_admin", "is_active", "login", "password")

    date_hierarchy = "tb_dentist__tb_person__birth_date"

    @admin.display(description="Full Name")
    def get_full_name(self, obj):
        return obj.tb_person.get_full_name()
    

admin.site.register(CustomUser, CustomUserAdmin)
