# Generated by Django 4.0.5 on 2022-07-01 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_cardetail_delete_cardetails'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'ordering': ['price'], 'verbose_name': 'Автомобили', 'verbose_name_plural': 'Автомобиль'},
        ),
        migrations.AlterModelOptions(
            name='cardetail',
            options={'ordering': ['car'], 'verbose_name': 'Автозапчасти', 'verbose_name_plural': 'Запчасть'},
        ),
        migrations.AlterModelOptions(
            name='detail',
            options={'ordering': ['type'], 'verbose_name': 'Детали', 'verbose_name_plural': 'Деталь'},
        ),
        migrations.AlterModelOptions(
            name='detailtype',
            options={'ordering': ['name'], 'verbose_name': 'Виды запчастей', 'verbose_name_plural': 'Вид'},
        ),
        migrations.AlterModelOptions(
            name='detailtypeproperty',
            options={'ordering': ['type'], 'verbose_name': 'Характеристики деталей', 'verbose_name_plural': 'Характеристика'},
        ),
        migrations.AlterModelOptions(
            name='detailtypepropertyvalue',
            options={'ordering': ['detail'], 'verbose_name': 'Значение характеристик деталей', 'verbose_name_plural': 'Значение'},
        ),
    ]