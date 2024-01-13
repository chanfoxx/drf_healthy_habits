# Generated by Django 4.2.9 on 2024-01-11 18:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0003_alter_habit_options_habit_action_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='lead_time',
            field=models.PositiveIntegerField(blank=True, help_text='Не более 120 секунд', null=True, validators=[django.core.validators.MaxValueValidator(120)], verbose_name='Время на выполнение'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='reward',
            field=models.CharField(blank=True, help_text='Вы можете использовать одно из трех: вознаграждение/приятная привычка/полезная привычка.', max_length=150, null=True, verbose_name='Вознаграждение за выполнение'),
        ),
    ]