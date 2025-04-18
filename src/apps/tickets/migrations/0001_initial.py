# Generated by Django 5.1.6 on 2025-02-24 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PopularDestination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point_code', models.CharField(help_text='Пример: FRU(Manas)', max_length=50, verbose_name='Код пункта')),
                ('point_name', models.CharField(max_length=100, verbose_name='Название пункта')),
                ('point_name_ru', models.CharField(max_length=100, verbose_name='Название пункта(RU)')),
                ('city_code', models.CharField(help_text='Пример: FRU', max_length=50, verbose_name='Код города')),
                ('city_name', models.CharField(help_text='Пример: Bishkek', max_length=100, verbose_name='Название города')),
                ('city_name_ru', models.CharField(help_text='Пример: Бишкек', max_length=100, verbose_name='Название города(RU)')),
                ('airport', models.BooleanField(default=False, verbose_name='Пункт является аэропортом')),
                ('own_route', models.BooleanField(default=False, verbose_name='Oбслуживает пункт собственные маршруты')),
                ('interline_route', models.BooleanField(default=False, verbose_name='Часть межлинейных маршрутов')),
                ('popular', models.BooleanField(default=False, verbose_name='Популярный пункт')),
                ('country_code', models.CharField(max_length=10, verbose_name='Код страны')),
                ('place_image', models.ImageField(upload_to='flight/popular/destination/%Y/%m/%d/')),
            ],
            options={
                'verbose_name': 'Популярное направление',
                'verbose_name_plural': 'Популярные направления',
                'ordering': ['id'],
            },
        ),
    ]
