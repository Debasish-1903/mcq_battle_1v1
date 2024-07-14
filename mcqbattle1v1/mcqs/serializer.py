from rest_framework import serializers


class OptionSerializer(serializers.Serializer):
    body=serializers.CharField()
    is_correct=serializers.BooleanField()


class McqSerializer(serializers.Serializer):
    id=serializers.UUIDField(read_only=True)
    body=serializers.CharField()
    explanation=serializers.CharField()
    options=OptionSerializer(many=True)    