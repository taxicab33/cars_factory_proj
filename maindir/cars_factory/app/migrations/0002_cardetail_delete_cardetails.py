# Generated by Django 4.0.5 on 2022-07-01 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=1)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.car')),
                ('detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.detail')),
            ],
        ),
        migrations.DeleteModel(
            name='CarDetails',
        ),
    ]
