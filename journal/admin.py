from django.contrib import admin
from journal.models import Publication
@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ['title']
# Register your models here.
