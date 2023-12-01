# Generated by Django 4.2.7 on 2023-12-01 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cadastro_usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='ativo',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='data_nascimento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='idade',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='nome',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='observacao',
            field=models.TextField(blank=True, null=True),
        ),
    ]