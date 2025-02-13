from rest_framework import serializers
from .models import GermanWord, Declination, Article, Pronoun, Conjunction, AdjectiveForm

class GermanWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = GermanWord
        fields = ['id', 'base_form', 'word_class', 'gender', 'metadata', 'user']
        read_only_fields = ['user']  # Stellt sicher, dass 'user' nicht vom Client gesetzt werden kann
        extra_kwargs = {
            'gender': {'required': False}  # Macht das Feld optional
        }

    def validate(self, data):
        word_class = data.get('word_class')
        gender = data.get('gender')

        # Wenn es ein Substantiv ist, muss gender vorhanden sein
        if word_class == 'NOUN' and not gender:
            raise serializers.ValidationError(
                {"gender": "Genus muss bei Substantiven angegeben werden."}
            )

        # Wenn es kein Substantiv ist, darf gender nicht gesetzt sein
        if word_class != 'NOUN' and gender:
            raise serializers.ValidationError(
                {"gender": "Genus darf nur bei Substantiven angegeben werden."}
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

        # Entferne 'user' aus validated_data, falls es vorhanden ist
        validated_data.pop('user', None)

        # Erstelle das GermanWord-Objekt
        return GermanWord.objects.create(user=user, **validated_data)

class DeclinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Declination
        fields = ['id', 'word', 'case', 'singular', 'plural']

from rest_framework import serializers
from .models import Article, Pronoun, Conjunction

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'article_type', 'case', 'gender', 'singular', 'plural']

class PronounSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pronoun
        fields = ['id', 'pronoun_type', 'case', 'gender', 'singular', 'plural']

class ConjunctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conjunction
        fields = ['id', 'conjunction_type', 'case_governed', 'word']
        
        

class AdjectiveFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdjectiveForm
        fields = ['id', 'word', 'case', 'number', 'gender', 'form']