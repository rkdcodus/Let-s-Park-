# Generated by Django 5.0 on 2023-12-17 08:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_user_id_alter_user_username'),
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='park',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='booking.park'),
        ),
    ]
