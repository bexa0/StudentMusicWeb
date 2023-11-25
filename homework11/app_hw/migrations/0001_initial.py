# Generated by Django 4.2.7 on 2023-11-25 12:55

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MusicalInstrument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('course', models.PositiveIntegerField()),
                ('grade', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)], verbose_name='Grade')),
                ('payment', models.BooleanField(default=False, verbose_name='Payment')),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, unique=True)),
                ('musical_instrument', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_hw.musicalinstrument')),
            ],
        ),
    ]
