# Generated by Django 4.2.9 on 2024-01-13 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0007_remove_habit_enjoyable_habit_habit_is_habit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='place',
            field=models.CharField(choices=[('дома', 'дома'), ('на кухне', 'на кухне'), ('на парковке', 'на парковке'), ('в бассейне', 'в бассейне'), ('в библиотеке', 'в библиотеке'), ('в кофейне', 'в кофейне'), ('в саду', 'в саду'), ('в парке', 'в парке'), ('на работе', 'на работе'), ('на прогулке', 'на прогулке'), ('в тренировочном зале', 'в тренировочном зале'), ('в магазине', 'в магазине')], default='дома', verbose_name='Место выполнения привычки'),
        ),
    ]