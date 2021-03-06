# Generated by Django 4.0.5 on 2022-07-01 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField(default=0)),
                ('manufacturer_margin', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='DetailType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DetailTypeProperty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='app.detailtype')),
            ],
        ),
        migrations.CreateModel(
            name='DetailTypePropertyValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255)),
                ('detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.detail')),
                ('property', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.detailtypeproperty')),
            ],
        ),
        migrations.AddField(
            model_name='detail',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='app.detailtype'),
        ),
        migrations.CreateModel(
            name='CarDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=1)),
                ('detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.detail')),
            ],
        ),
    ]
