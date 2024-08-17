from rest_framework import serializers
from .models import  Game
from django.contrib.auth.models import User
from mcqs.serializer import McqSerializer

from rest_framework import serializers
from .models import Attempt, ParticipantGameState

#Serializer for User
class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email=serializers.EmailField()
    first_name=serializers.CharField()
    last_name=serializers.CharField()

# Serializer for Games
class GameSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    owner = UserSerializer(read_only=True)
    status = serializers.ChoiceField(choices=Game.GAME_STATUS_CHOICES, default='waiting')
    questions = McqSerializer(many=True, read_only=True)
    participants = UserSerializer(many=True, read_only=True)
    max_participants = serializers.IntegerField()
    max_duration = serializers.DurationField()
    created_at = serializers.DateTimeField(read_only=True)
    started_at = serializers.DateTimeField(allow_null=True, required=False)
    completed_at = serializers.DateTimeField(allow_null=True, required=False)

    def create(self, validated_data):
        return Game.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.status = validated_data.get('status', instance.status)
        instance.max_participants = validated_data.get('max_participants', instance.max_participants)
        instance.max_duration = validated_data.get('max_duration', instance.max_duration)
        instance.started_at = validated_data.get('started_at', instance.started_at)
        instance.completed_at = validated_data.get('completed_at', instance.completed_at)
        instance.save()
        return instance
    


class AttemptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attempt
        fields = ['id', 'mcq', 'selected_option', 'created_at', 'participant']

class ParticipantGameStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParticipantGameState
        fields = ['game', 'participant', 'next_mcq', 'time_remaining', 'incorrect_answers']
