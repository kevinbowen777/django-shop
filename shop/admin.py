from typing import ClassVar

from django.contrib import admin

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display: ClassVar[list[str]] = ["name", "slug"]
    prepopulated_fields: ClassVar[dict[str, tuple]] = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display: ClassVar[list[str]] = [
        "name",
        "slug",
        "price",
        "available",
        "created",
        "updated",
    ]
    list_filter: ClassVar[list[str]] = ["available", "created", "updated"]
    list_editable: ClassVar[list[str]] = ["price", "available"]
    prepopulated_fields: ClassVar[dict[str, tuple]] = {"slug": ("name",)}
