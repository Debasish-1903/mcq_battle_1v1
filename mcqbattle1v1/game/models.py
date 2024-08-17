from django.db import models
from django.conf import settings
from django.utils import timezone
import uuid
from datetime import timedelta

class Game(models.Model):
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
    questions = models.ManyToManyField('mcqs.MCQs')  
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='participated_games')
    max_participants = models.PositiveIntegerField()
    max_duration = models.DurationField(default=timedelta(seconds=300)) 
    created_at = models.DateTimeField(auto_now_add=True)
    started_at = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Game {self.id} - {self.title}"

class Attempt(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mcq = models.ForeignKey('mcqs.MCQs', on_delete=models.CASCADE)
    selected_option = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    participant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class ParticipantGameState(models.Model):
    game = models.ForeignKey('Game', on_delete=models.CASCADE)
    participant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    next_mcq = models.ForeignKey('mcqs.MCQs', on_delete=models.SET_NULL, null=True, blank=True)
    time_remaining = models.DurationField(null=True, blank=True)  
    incorrect_answers = models.PositiveIntegerField(default=0)
    start_time = models.DateTimeField(null=True, blank=True) 
    total_duration = models.DurationField(default=timedelta(seconds=300))
    remaining_duration = models.DurationField(null=True, blank=True)  # This will be calculated dynamically
    current_question_timestamp = models.DateTimeField(null=True, blank=True)  

    class Meta:
        unique_together = ('game', 'participant')

    def update_remaining_duration(self):
        if self.start_time:
            elapsed_time = timezone.now() - self.start_time
            self.remaining_duration = max(self.total_duration - elapsed_time, timedelta(seconds=0))
            self.save()
