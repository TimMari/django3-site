# Generated by Django 4.0.2 on 2022-02-03 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Viz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Название')),
                ('text', models.TextField(verbose_name='Описание')),
                ('date', models.DateTimeField()),
                ('photo', models.ImageField(upload_to='vizitka/images/')),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]