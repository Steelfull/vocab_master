from django.db import migrations
from vocabulary.models import Article, Conjunction
from vocabulary.article_conjunction_data import ARTICLE_DATA, CONJUNCTION_DATA  # Importiere die Daten

def add_articles_and_conjunctions(apps, schema_editor):
    # Artikel hinzufügen
    for article_data in ARTICLE_DATA:
        Article.objects.create(**article_data)
    
    # Konjunktionen hinzufügen
    for conjunction_data in CONJUNCTION_DATA:
        Conjunction.objects.create(**conjunction_data)

class Migration(migrations.Migration):
    dependencies = [
        ('vocabulary', '0002_auto_20250213_0356'),  # Abhängigkeit von der vorherigen Migration
    ]

    operations = [
        migrations.RunPython(add_articles_and_conjunctions),
    ]