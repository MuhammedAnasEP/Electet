# Generated by Django 4.2.6 on 2023-10-23 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='company',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
