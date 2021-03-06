# Generated by Django 4.0.5 on 2022-07-01 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_car_options_alter_cardetail_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'ordering': ['price'], 'verbose_name': 'Автомобиль', 'verbose_name_plural': 'Автомобили'},
        ),
        migrations.AlterModelOptions(
            name='cardetail',
            options={'ordering': ['car'], 'verbose_name': 'Запчасть', 'verbose_name_plural': 'Автозапчасти'},
        ),
        migrations.AlterModelOptions(
            name='detail',
            options={'ordering': ['type'], 'verbose_name': 'Деталь', 'verbose_name_plural': 'Детали'},
        ),
        migrations.AlterModelOptions(
            name='detailtype',
            options={'ordering': ['name'], 'verbose_name': 'Вид', 'verbose_name_plural': 'Вид запчастей'},
        ),
        migrations.AlterModelOptions(
            name='detailtypeproperty',
            options={'ordering': ['type'], 'verbose_name': 'Характеристика', 'verbose_name_plural': 'Характеристики деталей'},
        ),
        migrations.AlterModelOptions(
            name='detailtypepropertyvalue',
            options={'ordering': ['detail'], 'verbose_name': 'Значение', 'verbose_name_plural': 'Значение характеристик деталей'},
        ),
    ]
