# Generated by Django 4.2.3 on 2023-08-11 01:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('financeiro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('rg', models.CharField(max_length=25)),
                ('cpf', models.CharField(max_length=25)),
                ('data_nascimento', models.DateField()),
                ('telefone', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=255)),
                ('status', models.BooleanField(choices=[(True, 'Ativo'), (False, 'Inativo')], default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('mensalidade', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='financeiro.mensalidade')),
            ],
        ),
    ]
