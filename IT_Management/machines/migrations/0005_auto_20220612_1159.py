# Generated by Django 3.1.6 on 2022-06-12 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0004_auto_20220612_1101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='machines',
            name='nom',
        ),
        migrations.AddField(
            model_name='machines',
            name='adresse',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='machines',
            name='date_de_la_mises_a_jour',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='machines',
            name='masque',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='machines',
            name='mises_a_jour',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='machines',
            name='nom_du_reseau',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='machines',
            name='technicien_qui_a_fait_la_mise_a_jour',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]