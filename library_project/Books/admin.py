from django.contrib import admin
from .models import Book



class BookAdmin(admin.ModelAdmin):

    actions = ['publish_selected']

    def publish_selected(self, request, queryset):
        queryset.update(status='published')

    publish_selected.short_description = "Publish the selected books"

# Register your models here.
admin.site.register(Book,BookAdmin)