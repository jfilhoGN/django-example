# Generated by Django 4.2.7 on 2023-12-07 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Times',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_time', models.CharField(max_length=100)),
                ('numero_integrantes', models.IntegerField(blank=True, null=True)),
                ('inicio_projeto', models.TextField(max_length=100000)),
            ],
        ),
    ]
