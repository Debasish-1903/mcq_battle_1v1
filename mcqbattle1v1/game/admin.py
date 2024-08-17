from django.contrib import admin
from .models import  Game
# Register your models here.

admin.site.register (Game)

'''
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'owner', 'status', 'created_at', 'started_at', 'completed_at')
    list_filter = ('status', 'created_at', 'started_at', 'completed_at')
    search_fields = ('title', 'owner__username')
    '''