# Generated by Django 4.1.7 on 2023-03-05 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Obj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(blank=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('address', models.TextField(blank=True)),
                ('status', models.CharField(max_length=100, null=True)),
                ('financed', models.CharField(max_length=100, null=True)),
                ('curator', models.TextField(blank=True)),
                ('email', models.TextField(blank=True)),
                ('objtype', models.CharField(max_length=100, null=True)),
                ('sporttype', models.CharField(max_length=100, null=True)),
                ('coordinatex', models.FloatField()),
                ('coordinatey', models.FloatField()),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
        ),
        migrations.DeleteModel(
            name='Search',
        ),
    ]
