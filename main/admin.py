from django.contrib import admin
from main.models import Letter


# Register your models here.
@admin.register(Letter)
class LetterAdmin(admin.ModelAdmin):
    list_display = ['id', 'sender', 'content', 'timestamp']
    list_display_links = ['id', 'sender']
