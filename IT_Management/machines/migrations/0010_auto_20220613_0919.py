# Generated by Django 3.1.6 on 2022-06-13 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0009_technicien'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='technicien',
            name='id',
        ),
        migrations.AlterField(
            model_name='technicien',
            name='technicien',
            field=models.AutoField(editable=False, primary_key=True, serialize=False),
        ),
    ]