# Generated by Django 4.2.9 on 2024-01-19 07:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('habits', '0009_alter_habit_place'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Создатель привычки'),
        ),
    ]
