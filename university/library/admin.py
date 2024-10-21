from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Book, User, Forma

def update_register(modeladmin, request, queryset):
    queryset.update(is_active=False)
@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    search_fields = ( "title", "author")
    list_display = ("title", "author", "count", "pages")
    actions = [update_register]


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ("first_name", "last_name")
    list_display = ("first_name", "last_name", "role")
    list_filter = ("role",)


@admin.register(Forma)
class FormaAdmin(ImportExportModelAdmin):
    search_fields = ("full_name",)
    list_display = ("full_name", "age", "phone", "address")



