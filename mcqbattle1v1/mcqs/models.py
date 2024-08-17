from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import uuid




class MCQs(models.Model):
    id=models.UUIDField(primary_key=True,
                        default=uuid.uuid4,
                        editable=False)
    body=models.TextField()
    explanation=models.TextField()
    options=models.JSONField()



'''class Game(models.Model):
    GAME_STATUS_CHOICES = [
        ('waiting', 'Waiting'),
        ('active', 'Active'),
        ('completed', 'Completed'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='owned_games', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=GAME_STATUS_CHOICES, default='waiting')
    questions = models.ManyToManyField('MCQs')  
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='participated_games')
    max_participants = models.PositiveIntegerField()
    max_duration = models.DurationField()  
    created_at = models.DateTimeField(auto_now_add=True)
    started_at = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)

def __str__(self):
    return f"Game {self.id} - {self.title}"'''
