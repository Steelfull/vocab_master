from django.db import migrations
from vocabulary.models import Pronoun
from vocabulary.pronoun_data import PRONOUN_DATA  # Importiere die Pronomen-Daten

def add_pronouns(apps, schema_editor):
    for pronoun_data in PRONOUN_DATA:
        Pronoun.objects.create(**pronoun_data)

class Migration(migrations.Migration):
    dependencies = [
        ('vocabulary', '0001_initial'),  # Abhängigkeit von der vorherigen Migration
    ]

    operations = [
        migrations.RunPython(add_pronouns),
    ]