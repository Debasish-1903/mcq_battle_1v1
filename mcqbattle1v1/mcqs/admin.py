from django.contrib import admin
from .models import  MCQs

@admin.register(MCQs)
class MCQsAdmin(admin.ModelAdmin):
    list_display = ('id', 'body', 'explanation') #one tuple
    search_fields = ('body', 'explanation')
