# Generated by Django 4.2.3 on 2023-07-26 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treinos', '0003_alter_treino_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treino_aluno',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
