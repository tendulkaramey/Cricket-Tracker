# Generated by Django 4.2.4 on 2023-11-17 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_tournamentfixture_team_won_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournamentmatch',
            name='extra',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]