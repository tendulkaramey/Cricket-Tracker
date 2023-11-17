# Generated by Django 4.2.4 on 2023-11-17 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_tournamentfixture_team_won_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournamentfixture',
            name='team_won',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_won', to='api.team'),
        ),
        migrations.AlterField(
            model_name='tournamentfixture',
            name='toss_won',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='toss_won', to='api.team'),
        ),
    ]