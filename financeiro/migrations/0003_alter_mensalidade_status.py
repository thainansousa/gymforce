# Generated by Django 4.2.3 on 2023-07-30 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0002_alter_mensalidade_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensalidade',
            name='status',
            field=models.BooleanField(choices=[(True, 'Ativo'), (False, 'Inativo')], default=True),
        ),
    ]
