# Generated by Django 3.0.8 on 2020-07-18 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendedor', '0002_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cod_cliente',
            field=models.CharField(max_length=36, primary_key=True, serialize=False),
        ),
    ]
