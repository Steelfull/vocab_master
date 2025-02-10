from rest_framework import serializers
from .models import GermanWord

class GermanWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = GermanWord
        fields = ['id', 'base_form', 'word_class', 'gender', 'metadata', 'user']
        read_only_fields = ['user']
        extra_kwargs = {
            'gender': {'required': False}  # Macht das Feld optional
        }

    def validate(self, data):
        # Wenn es ein Substantiv ist, muss gender vorhanden sein
        if data.get('word_class') == 'NOUN' and not data.get('gender'):
            raise serializers.ValidationError(
                {"gender": "Genus muss bei Substantiven angegeben werden"}
            )
        return data
    
def create(self, validated_data):
    user = self.context['request'].user
    metadata = validated_data.get("metadata", {})

    # Extrahiere word_class aus metadata, falls es dort ist
    word_class = validated_data.get("word_class") or metadata.get("word_class")

    if not word_class:
        raise serializers.ValidationError({"word_class": "Dieses Feld wird benötigt."})

    validated_data["word_class"] = word_class  # Setze das extrahierte Feld

    return GermanWord.objects.create(user=user, **validated_data)
