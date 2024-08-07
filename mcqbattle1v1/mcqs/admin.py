from django.contrib import admin
from .models import Game, MCQs

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'owner', 'status', 'created_at', 'started_at', 'completed_at')
    list_filter = ('status', 'created_at', 'started_at', 'completed_at')
    search_fields = ('title', 'owner__username')

@admin.register(MCQs)
class MCQsAdmin(admin.ModelAdmin):
    list_display = ('id', 'body', 'explanation')
    search_fields = ('body', 'explanation')
