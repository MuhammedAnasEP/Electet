# Generated by Django 4.2.6 on 2023-10-23 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='photo')),
                ('image1', models.ImageField(default=0, null=True, upload_to='photo')),
                ('image2', models.ImageField(default=0, null=True, upload_to='photo')),
                ('image3', models.ImageField(default=0, null=True, upload_to='photo')),
                ('price', models.FloatField()),
                ('stock', models.IntegerField()),
                ('slug', models.SlugField()),
                ('description', models.CharField(max_length=200, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.categorys')),
            ],
        ),
    ]