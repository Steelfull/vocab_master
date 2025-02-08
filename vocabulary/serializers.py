from rest_framework import serializers
from .models import GermanWord

class GermanWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = GermanWord
        fields = ['id', 'base_form', 'word_class', 'gender', 'metadata', 'user']
        read_only_fields = ['user']
    
    def create(self, validated_data):
        # Automatisch den aktuellen User zuweisen
        user = self.context['request'].user
        return GermanWord.objects.create(user=user, **validated_data)