# Generated by Django 4.2.7 on 2025-03-19 02:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='populardestination',
            name='country_name',
            field=models.CharField(default=django.utils.timezone.now, help_text='Пример: Кыргызстан', max_length=100, verbose_name='Название страны'),
            preserve_default=False,
        ),
    ]
