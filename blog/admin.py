from django.contrib import admin

from blog.models import BlogPost


@admin.register(BlogPost)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "slug",)
    list_filter = ("published",)
    search_fields = ("title",)

