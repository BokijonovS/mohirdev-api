# Generated by Django 5.0.6 on 2024-06-20 13:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_rating_lesson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='app.lesson'),
        ),
    ]
