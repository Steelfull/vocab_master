# Generated by Django 5.1.6 on 2025-02-10 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocabulary', '0003_remove_germanword_pronoun_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='germanword',
            name='gender',
            field=models.CharField(max_length=10),
        ),
    ]
