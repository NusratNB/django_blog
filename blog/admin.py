from django.contrib import admin

from .models import Author, Post, Tag

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "date", "tag",)
    list_display = ("title", "date", "author", )

admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)

