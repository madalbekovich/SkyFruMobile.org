# Generated by Django 4.2.7 on 2025-03-19 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TechSupportFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('phone', models.IntegerField(verbose_name='Номер телефона')),
                ('ReasonDesc', models.TextField(verbose_name='Причина')),
                ('img', models.ImageField(upload_to='feedback/reason/')),
            ],
            options={
                'verbose_name': 'Запрос в техническую поддержку',
                'verbose_name_plural': 'Запросы в техническую поддержку',
                'ordering': ['id'],
            },
        ),
    ]
