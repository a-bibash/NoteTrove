# Generated by Django 4.1.4 on 2023-09-23 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0015_alter_room_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='digital',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
