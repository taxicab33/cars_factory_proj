# Generated by Django 4.0.5 on 2022-07-01 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_car_options_alter_cardetail_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='detailtype',
            options={'ordering': ['name'], 'verbose_name': 'Вид', 'verbose_name_plural': 'Виды запчастей'},
        ),
    ]